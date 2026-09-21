from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "ticket", "amount", "currency", "payment_method", "status", "paid_at", "created_at")
    search_fields = ("provider_payment_id", "ticket__id")
    list_filter = ("payment_method", "status", "currency")