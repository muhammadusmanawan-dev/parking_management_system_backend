from django.db import models


class ParkingSpot(models.Model):
    SPOT_TYPE_CHOICES = [
        ("car", "Car"),
        ("motorcycle", "Motorcycle"),
        ("truck", "Truck"),
        ("van", "Van"),
        ("bus", "Bus"),
    ]

    spot_number = models.CharField(max_length=10, unique=True)
    spot_type = models.CharField(max_length=20, choices=SPOT_TYPE_CHOICES)

    SPOT_STATUS_CHOICES = [
        ("available", "Available"), 
        ("occupied", "Occupied"),
        ("reserved", "Reserved"),
    ]
    status = models.CharField(max_length=20, choices=SPOT_STATUS_CHOICES, default="available")  


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   
    def __str__(self):
        return self.spot_number
    