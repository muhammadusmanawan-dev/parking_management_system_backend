from django.conf import settings

from .base import PaymentService


class SafepayPaymentService(PaymentService):
    def create_payment(self,amount,currency,reference,):
        if not settings.SAFEPAY_SECRET_KEY:
            raise ValueError(
                "SAFEPAY_SECRET_KEY is not configured."
            )

        raise NotImplementedError(
            "Safepay integration is not implemented yet."
        )

    def check_payment_status(self,payment_id):
        if not settings.SAFEPAY_SECRET_KEY:
            raise ValueError(
                "SAFEPAY_SECRET_KEY is not configured."
            )

        raise NotImplementedError(
            "Safepay integration is not implemented yet."
        )