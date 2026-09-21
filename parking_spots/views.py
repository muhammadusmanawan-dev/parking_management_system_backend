from rest_framework.permissions import IsAuthenticated
from .models import ParkingSpot
from .serializers import ParkingSpotSerializer
from rest_framework.viewsets import ModelViewSet


class ParkingSpotViewSet(ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    permission_classes = [IsAuthenticated]
