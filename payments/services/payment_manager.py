from django.utils import timezone

from ..models import Payment, PaymentStatus
from .fare_service import FareService
from .factory import PaymentServiceFactory


class PaymentManager:

    @staticmethod
    def create_payment(ticket, payment_method):
        amount = FareService.calculate_fare(ticket)

        service = PaymentServiceFactory.get_service(payment_method)

        result = service.create_payment(
            amount=amount,
            currency="PKR",
            reference=f"TICKET-{ticket.id}",
        )

        provider_status = result.get("status")

        payment_status = (
            PaymentStatus.PAID
            if provider_status == "succeeded"
            else PaymentStatus.PENDING
        )

        paid_at = (
            timezone.now()
            if provider_status == "succeeded"
            else None
        )

        payment = Payment.objects.create(
            ticket=ticket,
            amount=amount,
            currency="PKR",
            payment_method=payment_method,
            status=payment_status,
            provider_payment_id=result["payment_id"],
            paid_at=paid_at,
        )

        return payment, result

    @staticmethod
    def check_payment_status(payment):
        service = PaymentServiceFactory.get_service(Payment.payment_method)
        result = service.check_payment_status(payment.provider_payment_id)
        provider_status = result.get("status")

        if provider_status == "succeeded":
            payment.status = PaymentStatus.PAID
            payment.paid_at = payment.paid_at or timezone.now()

        elif provider_status in ["failed", "canceled"]:
            payment.status = PaymentStatus.FAILED

        payment.save(
            update_fields=[
                "status",
                "paid_at",
            ]
        )

        return payment, result
