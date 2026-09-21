from rest_framework import serializers

from tickets.models import Ticket

from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment

        # Provide: ticket, payment_method
        fields = [
            "id",
            "ticket",
            "amount",
            "currency",
            "payment_method",
            "status",
            "provider_payment_id",
            "paid_at",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "amount",
            "currency",
            "status",
            "provider_payment_id",
            "paid_at",
            "created_at",
            "updated_at",
        ]

    def validate_ticket(self, ticket):
        if ticket.status != "completed":
            raise serializers.ValidationError(
                "Payment can only be created for a completed ticket."
            )

        return ticket

    def validate(self, attrs):
        ticket = attrs["ticket"]

        if Payment.objects.filter(ticket=ticket).exists():
            raise serializers.ValidationError(
                {"ticket": ("A payment already exists for this ticket.")}
            )

        return attrs
