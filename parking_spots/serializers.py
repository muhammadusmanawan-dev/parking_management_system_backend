from rest_framework import serializers

from .models import ParkingSpot


class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot

        fields = [
            "id",
            "spot_number",
            "spot_type",
            "status",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]
