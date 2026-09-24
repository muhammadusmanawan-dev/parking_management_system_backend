from decimal import Decimal

import stripe
from django.conf import settings

from .base import PaymentService
from config.exception import PaymentProviderError

class StripePaymentService(PaymentService):
    def create_payment(self, amount,currency,reference):
        stripe.api_key=settings.STRIPE_SECRET_KEY

        try:
            amount=Decimal(amount)
            smallest_unit_amount=int(amount*100)
            
            payment_intent=stripe.PaymentIntent.create(
                amount=smallest_unit_amount,
                currency=currency.lower(),
                metadata={"reference":reference}
            )
            return {
                "payment_id":payment_intent.id,
                "client_secret":payment_intent.client_secret,
                "status":payment_intent.status
            }
        except stripe.StripeError:
            raise PaymentProviderError()

    def check_payment_status(self, payment_id):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        try:
            payment_intent = stripe.PaymentIntent.retrieve(payment_id)

            return {
                "payment_id": payment_intent.id,
                "status": payment_intent.status,
            }

        except stripe.StripeError:
            raise PaymentProviderError()
