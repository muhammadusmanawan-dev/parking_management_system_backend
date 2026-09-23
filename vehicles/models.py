from django.db import models

from customers.models import Customer


class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ("car", "Car"),
        ("motorcycle", "Motorcycle"),
        ("truck", "Truck"),
        ("van", "Van"),
        ("bus", "Bus"),
    ]
    
    license_plate = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.license_plate
