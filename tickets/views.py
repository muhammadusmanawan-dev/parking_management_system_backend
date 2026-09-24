from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ticket, TicketStatus
from .serializers import TicketSerializer
from .services.ticket_service import TicketService

from .ticket_entry_serializer import ParkingEntrySerializer 
from .services.ticket_entry_service import TicketEntryService

class TicketListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ticket = TicketService.create_ticket(serializer)

        return Response(
            TicketSerializer(ticket).data,
            status=status.HTTP_201_CREATED,
        )
class TicketDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, ticket_id):
        ticket = get_object_or_404(
            Ticket,
            id=ticket_id,
        )
        serializer = TicketSerializer(ticket)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class TicketCheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, ticket_id):
        ticket = get_object_or_404(
            Ticket,
            id=ticket_id,
        )
        
        ticket = TicketService.checkout_ticket(ticket)

        return Response(
            TicketSerializer(ticket).data,
            status=status.HTTP_200_OK,
        )

class ParkingEntryView(APIView): 
    permission_classes = [IsAuthenticated] 
    def post(self, request): 
        serializer = ParkingEntrySerializer( data=request.data ) 
        serializer.is_valid( raise_exception=True ) 
        result = TicketEntryService.create_entry(
            **serializer.validated_data
        )
        customer = result["customer"]
        vehicle = result["vehicle"]
        parking_spot = result["parking_spot"]
        ticket = result["ticket"]

        response_data = {
                    "message": "Vehicle entered successfully.",
                    "customer": {
                        "id": customer.id,
                        "name": customer.name,
                        "phone_number": customer.phone_number,
                    },
                    "vehicle": {
                        "id": vehicle.id,
                        "license_plate": vehicle.license_plate,
                        "vehicle_type": vehicle.vehicle_type,
                    },
                    "parking_spot": {
                        "id": parking_spot.id,
                        "spot_number": parking_spot.spot_number,
                        "spot_type": parking_spot.spot_type,
                        "status": parking_spot.status,
                    },
                    "ticket": {
                        "id": ticket.id,
                        "entry_time": ticket.entry_time,
                        "status": ticket.status,
                    },
                }
        return Response(
            response_data,
            status=status.HTTP_201_CREATED,
        )
