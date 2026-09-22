from django.db import models
from tickets.models import Ticket

class PaymentMethod(models.TextChoices):
    STRIPE="stripe","Stripe"
    SAFEPAY="safepay","Safepay"

class PaymentStatus(models.TextChoices):
    PENDING="pending", "Pending"
    PAID="paid", "Paid"
    FAILED="failed", "Failed"
class Payment(models.Model):

    ticket = models.OneToOneField(
        Ticket,
        on_delete=models.PROTECT,
        related_name="payment",
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    currency = models.CharField(
        max_length=3,
        default="PKR",
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PaymentMethod.choices, default=PaymentMethod.STRIPE
    )
    status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING,
    )

    provider_payment_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        unique=True,
    )
    paid_at = models.DateTimeField(
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"Payment #{self.id}"
