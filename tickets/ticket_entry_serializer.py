from rest_framework import serializers
from vehicles.models import Vehicle

class ParkingEntrySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=15)
    license_plate = serializers.CharField(max_length=20)
    vehicle_type = serializers.ChoiceField(
        choices=Vehicle.VEHICLE_TYPE_CHOICES
    )
