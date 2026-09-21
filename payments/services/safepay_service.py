from .base import PaymentService


class SafepayPaymentService(PaymentService):

    def create_payment(self, amount, currency, reference):
        pass

    def check_payment_status(self, payment_id):
        pass