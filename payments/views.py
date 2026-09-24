from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Payment
from .serializers import PaymentSerializer
from .services.payment_manager import PaymentManager
from config.decorators import handle_exceptions
class PaymentListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    @handle_exceptions
    def post(self, request):
        serializer=PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ticket=serializer.validated_data["ticket"]
        payment_method=serializer.validated_data["payment_method"]

        payment, result=PaymentManager.create_payment(
            ticket=ticket,
            payment_method=payment_method
        )
        
        return Response(
            {
                "payment": PaymentSerializer(payment).data,
                "provider": result,
            },
            status=status.HTTP_201_CREATED,
        )

class PaymentDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, payment_id):
        payment = get_object_or_404(
            Payment,
            id=payment_id,
        )

        serializer = PaymentSerializer(payment)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class PaymentStatusView(APIView):
    permission_classes = [IsAuthenticated]

    @handle_exceptions
    def get(self, request, payment_id):
        payment = get_object_or_404(
            Payment,
            id=payment_id,
        )

        payment, result = PaymentManager.check_payment_status(
            payment
        )
        
        return Response(
            {
                "payment": PaymentSerializer(payment).data,
                "provider": result,
            },
            status=status.HTTP_200_OK,
        )
