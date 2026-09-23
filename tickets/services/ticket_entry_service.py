from django.db import transaction

from customers.models import Customer
from parking_spots.models import ParkingSpot, ParkingSpotStatus
from vehicles.models import Vehicle

from ..serializers import TicketSerializer
from .ticket_service import TicketService


class TicketEntryService:

    @staticmethod
    @transaction.atomic
    def create_entry(name,phone_number,license_plate,vehicle_type,):
        customer, customer_created = Customer.objects.get_or_create(
            phone_number=phone_number,
            defaults={
                "name": name,
            },
        )

        vehicle, vehicle_created = Vehicle.objects.get_or_create(
            license_plate=license_plate,
            defaults={
                "vehicle_type": vehicle_type,
            },
        )

        if not vehicle_created and vehicle.vehicle_type != vehicle_type:
            raise ValueError(
                "Vehicle type does not match the registered vehicle."
            )

        parking_spot = ParkingSpot.objects.filter(spot_type=vehicle_type,status=ParkingSpotStatus.AVAILABLE,).first()

        if parking_spot is None:
            raise ValueError(
                "No parking spot available."
            )

        ticket_serializer = TicketSerializer(data={"customer":customer.id, "vehicle": vehicle.id,"parking_spot": parking_spot.id,})
        ticket_serializer.is_valid(raise_exception=True)
        ticket = TicketService.create_ticket(ticket_serializer)
        return {
            "customer": customer,
            "vehicle": vehicle,
            "parking_spot": parking_spot,
            "ticket": ticket,
        }
