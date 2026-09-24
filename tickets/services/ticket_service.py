from django.db import transaction
from django.utils import timezone

from parking_spots.models import ParkingSpotStatus
from tickets.models import TicketStatus

from config.exception import TicketAlreadyCompleted
class TicketService:

    @staticmethod
    @transaction.atomic
    def create_ticket(serializer):
        ticket = serializer.save()
        parking_spot = ticket.parking_spot
        parking_spot.status = ParkingSpotStatus.OCCUPIED
        parking_spot.save(update_fields=["status", "updated_at"])
        return ticket
    
    @staticmethod
    @transaction.atomic
    def checkout_ticket(ticket):
        if ticket.status != TicketStatus.ACTIVE:
            raise TicketAlreadyCompleted()
        
        ticket.exit_time = timezone.now()
        ticket.status = TicketStatus.COMPLETED

        ticket.save(
            update_fields=[
                "exit_time",
                "status",
                "updated_at",
            ]
        )

        parking_spot = ticket.parking_spot
        parking_spot.status = ParkingSpotStatus.AVAILABLE

        parking_spot.save(
            update_fields=[
                "status",
                "updated_at",
            ]
        )
        return ticket
