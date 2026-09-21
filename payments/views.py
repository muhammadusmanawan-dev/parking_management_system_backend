from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Payment
from .serializers import PaymentSerializer
from .services.fare_service import FareService
from .services.factory import PaymentServiceFactory


class PaymentListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ticket = serializer.validated_data["ticket"]
        payment_method = serializer.validated_data["payment_method"]

        try:
            amount = FareService.calculate_fare(ticket)
            service = PaymentServiceFactory.get_service(payment_method)
            result = service.create_payment(amount=amount, currency="PKR", reference=f"TICKET-{ticket.id}")
        except NotImplementedError as error:
            return Response({"detail": str(error)}, status=status.HTTP_501_NOT_IMPLEMENTED)
        except Exception as error:
            return Response({"detail": "Payment provider request failed.", "error": str(error)}, status=status.HTTP_502_BAD_GATEWAY)

        provider_status = result.get("status")
        payment_status = "paid" if provider_status == "succeeded" else "pending"
        paid_at = timezone.now() if provider_status == "succeeded" else None

        payment = Payment.objects.create(ticket=ticket, amount=amount, currency="PKR", payment_method=payment_method, status=payment_status, provider_payment_id=result["payment_id"], paid_at=paid_at)

        return Response({"payment": PaymentSerializer(payment).data, "provider": result}, status=status.HTTP_201_CREATED)


class PaymentDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, payment_id):
        payment = get_object_or_404(Payment, id=payment_id)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PaymentStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, payment_id):
        payment = get_object_or_404(Payment, id=payment_id)
        service = PaymentServiceFactory.get_service(payment.payment_method)

        try:
            result = service.check_payment_status(payment.provider_payment_id)
        except NotImplementedError as error:
            return Response({"detail": str(error)}, status=status.HTTP_501_NOT_IMPLEMENTED)
        except Exception as error:
            return Response({"detail": "Payment provider request failed.", "error": str(error)}, status=status.HTTP_502_BAD_GATEWAY)

        provider_status = result.get("status")

        if provider_status == "succeeded":
            payment.status = "paid"
            payment.paid_at = payment.paid_at or timezone.now()
        elif provider_status in ["failed", "canceled"]:
            payment.status = "failed"

        payment.save(update_fields=["status", "paid_at", "updated_at"])

        return Response({"payment": PaymentSerializer(payment).data, "provider": result}, status=status.HTTP_200_OK)