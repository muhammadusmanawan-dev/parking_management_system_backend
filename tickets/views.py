from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ticket
from .serializers import TicketSerializer


class TicketListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tickets=Ticket.objects.all()
        serializer=TicketSerializer(tickets,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer=TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        with transaction.atomic():
            ticket=serializer.save()
            parking_spot=ticket.parking_spot
            parking_spot.status="occupied"
            parking_spot.save(update_fields=["status","updated_at"])
            return Response(TicketSerializer(ticket).data,status=status.HTTP_201_CREATED)
        
class TicketDetailView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request,ticket_id):
        ticket=get_object_or_404(Ticket,id=ticket_id)
        serializer=TicketSerializer(ticket)
        return Response(serializer.data,status=status.HTTP_200_OK)
