from django.contrib import admin

from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "license_plate",
        "customer",
        "vehicle_type",
        "created_at",
    )

    search_fields = (
        "license_plate",
        "customer__name",
        "customer__phone_number",
    )

    list_filter = ("vehicle_type",)
