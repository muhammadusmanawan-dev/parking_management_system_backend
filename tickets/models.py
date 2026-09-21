from django.db import models

from parking_spots.models import ParkingSpot
from vehicles.models import Vehicle


class Ticket(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("completed", "Completed"),
    ]

    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE,related_name="tickets")
    parking_spot = models.ForeignKey(ParkingSpot,on_delete=models.PROTECT,related_name="tickets")

    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True,blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="active",)

    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return f"Ticket #{self.id}"