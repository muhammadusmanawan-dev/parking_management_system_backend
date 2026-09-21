from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from tickets.models import Ticket

from .models import Payment
from .serializers import PaymentSerializer
from .services.fare_service import FareService
from .services.factory import PaymentServiceFactory


class PaymentListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payments = Payment.objects.all()

        serializer = PaymentSerializer(payments,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ticket = serializer.validated_data["ticket"]
        
        amount = FareService.calculate_fare(ticket)
        payment_method = serializer.validated_data["payment_method"]
        service = PaymentServiceFactory.get_service(payment_method)
        result = service.create_payment(amount=amount,currency="PKR",reference=f"TICKET-{ticket.id}",)

        payment = Payment.objects.create(
            ticket=ticket,
            amount=amount,
            currency="PKR",
            payment_method=payment_method,
            status="pending",
            provider_payment_id=result["payment_id"],
        )

        return Response({"payment": PaymentSerializer(payment).data,"provider": result,},status=status.HTTP_201_CREATED,)


class PaymentDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, payment_id):
        payment = get_object_or_404(Payment,id=payment_id)
        serializer = PaymentSerializer(payment)

        return Response(serializer.data, status=status.HTTP_200_OK,)
    