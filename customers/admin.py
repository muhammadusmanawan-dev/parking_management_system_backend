from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "phone_number",
        "created_at",
    )

    search_fields = (
        "name",
        "phone_number",
    )
