from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ticket, TicketStatus
from .serializers import TicketSerializer
from .services import TicketService


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
