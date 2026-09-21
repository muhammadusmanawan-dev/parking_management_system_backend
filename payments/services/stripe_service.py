from .base import PaymentService


class StripePaymentService(PaymentService):

    def create_payment(self, amount, currency, reference):
        pass

    def check_payment_status(self, payment_id):
        pass