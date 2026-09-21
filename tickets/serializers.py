from rest_framework import serializers

from parking_spots.models import ParkingSpot
from vehicles.models import Vehicle

from .models import Ticket


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

        if parking_spot.status != "available":
            raise serializers.ValidationError({"parking_spot": ("This parking spot is not available.")})

        active_ticket = Ticket.objects.filter(vehicle=vehicle,status="active",).exists()

        if active_ticket:
            raise serializers.ValidationError({"vehicle": ("This vehicle already has an active ticket.")})
        
        return attrs