from django.contrib import admin

from .models import ParkingSpot


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "spot_number",
        "spot_type",
        "status",
        "created_at",
        "updated_at",
    )

    search_fields = ("spot_number", "spot_type", "status")
    list_filter = ("spot_type", "status", "created_at", "updated_at")
