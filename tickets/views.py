from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ticket, TicketStatus
from .serializers import TicketSerializer

from parking_spots.models import ParkingSpot, ParkingSpotStatus
class TicketListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            ticket = serializer.save()
            parking_spot = ticket.parking_spot
            parking_spot.status = ParkingSpotStatus.OCCUPIED
            parking_spot.save(update_fields=["status", "updated_at"])
            return Response(
                TicketSerializer(ticket).data, status=status.HTTP_201_CREATED
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

        if ticket.status != TicketStatus.ACTIVE:
            return Response(
                {"detail": ("This ticket has already been completed.")},
                status=status.HTTP_400_BAD_REQUEST,
            )

        with transaction.atomic():
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

        return Response(
            TicketSerializer(ticket).data,
            status=status.HTTP_200_OK,
        )
