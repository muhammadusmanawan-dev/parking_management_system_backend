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

        try:
            ticket = TicketService.checkout_ticket(ticket)

        except ValueError as error:
            return Response(
                {"detail": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )

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
            name=serializer.validated_data["name"], 
            phone_number=serializer.validated_data["phone_number"], 
            license_plate=serializer.validated_data["license_plate"], 
            vehicle_type=serializer.validated_data["vehicle_type"],
            ) 
        
        return Response( { "message": "Vehicle entered successfully.",
                           "customer": { 
                               "id": result["customer"].id, 
                               "name": result["customer"].name, 
                               "phone_number": result["customer"].phone_number, }, 
                            "vehicle": {
                                "id": result["vehicle"].id, 
                                "license_plate": result["vehicle"].license_plate, 
                                "vehicle_type": result["vehicle"].vehicle_type, }, 
                            "parking_spot": {
                                 "id": result["parking_spot"].id, 
                                 "spot_number": result["parking_spot"].spot_number, 
                                 "spot_type": result["parking_spot"].spot_type, 
                                 "status": result["parking_spot"].status, }, 
                            "ticket": { 
                                "id": result["ticket"].id, 
                                "entry_time": result["ticket"].entry_time, 
                                "status": result["ticket"].status, },
                            }, 
                            status=status.HTTP_201_CREATED, )
