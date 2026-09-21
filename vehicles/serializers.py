from rest_framework import serializers

from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle

        fields = [
            "id",
            "customer",
            "license_plate",
            "vehicle_type",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]
