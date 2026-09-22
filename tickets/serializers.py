from rest_framework import serializers

from .models import Ticket, TicketStatus
from parking_spots.models import ParkingSpot, ParkingSpotStatus 

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket

        fields = [
            "id",
            "vehicle",
            "parking_spot",
            "entry_time",
            "exit_time",
            "status",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "entry_time",
            "exit_time",
            "status",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        vehicle = attrs.get("vehicle")
        parking_spot = attrs.get("parking_spot")

        if parking_spot.status != ParkingSpotStatus.AVAILABLE:
            raise serializers.ValidationError(
                {"parking_spot": ("This parking spot is not available.")}
            )

        active_ticket = Ticket.objects.filter(
            vehicle=vehicle,
            status=TicketStatus.ACTIVE,
        ).exists()

        if active_ticket:
            raise serializers.ValidationError(
                {"vehicle": ("This vehicle already has an active ticket.")}
            )

        return attrs
