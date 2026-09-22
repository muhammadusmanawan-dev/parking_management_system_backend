from django.db import models

class ParkingSpotStatus(models.TextChoices):
    AVAILABLE="available","Available"
    OCCUPIED="occupied","Occupied"
    RESERVED="reserved","Reserved"

class ParkingSpotType(models.TextChoices):
      CAR="car", "Car"
      MOTORCYCLE="motorcycle", "Motorcycle"
      TRUCK="truck", "Truck"
      VAN="van", "Van"
      BUS="bus", "Bus"
class ParkingSpot(models.Model):

    spot_number = models.CharField(max_length=10, unique=True)
    spot_type = models.CharField(max_length=20, choices=ParkingSpotType.choices)

    status = models.CharField(
        max_length=20, choices=ParkingSpotStatus.choices, default=ParkingSpotStatus.AVAILABLE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.spot_number
