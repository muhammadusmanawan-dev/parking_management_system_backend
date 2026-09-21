from .safepay_service import SafepayPaymentService
from .stripe_service import StripePaymentService


class PaymentServiceFactory:

    @staticmethod
    def get_service(payment_method):

        if payment_method == "stripe":
            return StripePaymentService()

        if payment_method == "safepay":
            return SafepayPaymentService()

        raise ValueError("Unsupported payment method.")
