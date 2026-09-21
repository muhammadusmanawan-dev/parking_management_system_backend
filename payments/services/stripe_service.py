from decimal import Decimal

import stripe
from django.conf import settings

from .base import PaymentService


class StripePaymentService(PaymentService):

    def create_payment(self, amount, currency, reference):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        amount = Decimal(amount)
        amount_in_smallest_unit = int(amount * 100)
        payment_intent = stripe.PaymentIntent.create(
            amount=amount_in_smallest_unit,
            currency=currency.lower(),
            metadata={
                "reference": reference,
            },
        )

        return {
            "payment_id": payment_intent.id,
            "client_secret": payment_intent.client_secret,
            "status": payment_intent.status,
        }

    def check_payment_status(self, payment_id):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        payment_intent = stripe.PaymentIntent.retrieve(payment_id)

        return {
            "payment_id": payment_intent.id,
            "status": payment_intent.status,
        }
