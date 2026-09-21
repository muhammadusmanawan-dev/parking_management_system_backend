from abc import ABC, abstractmethod


class PaymentService(ABC):

    @abstractmethod
    def create_payment(self, amount, currency, reference):
        pass

    @abstractmethod
    def check_payment_status(self, payment_id):
        pass