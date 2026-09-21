from rest_framework.routers import DefaultRouter

from parking_spots.views import ParkingSpotViewSet

router = DefaultRouter()
router.register(r"parking-spots", ParkingSpotViewSet, basename="parking-spot")
urlpatterns = router.urls
