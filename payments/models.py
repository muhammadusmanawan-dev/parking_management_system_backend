from django.db import models
from tickets.models import Ticket
class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ("stripe", "Stripe"),
        ("safepay", "Safepay"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("failed", "Failed"),
    ]

    ticket = models.OneToOneField(Ticket,on_delete=models.PROTECT,related_name="payment",)
    amount = models.DecimalField(max_digits=10,decimal_places=2,)
    currency = models.CharField(max_length=3,default="PKR",)

    payment_method = models.CharField(max_length=20,choices=PAYMENT_METHOD_CHOICES,)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="pending",)

    provider_payment_id = models.CharField(max_length=255,blank=True,null=True,unique=True,)
    paid_at = models.DateTimeField(null=True,blank=True,)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return f"Payment #{self.id}"
    