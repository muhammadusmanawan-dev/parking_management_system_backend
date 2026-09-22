from django.urls import path

from .views import TicketListCreateView, TicketCheckoutView, TicketDetailView, ParkingEntryView
urlpatterns = [
    path("tickets/", TicketListCreateView.as_view(), name="ticket_list_create"),
    path(
        "tickets/<int:ticket_id>/",
        TicketDetailView.as_view(),
        name="ticket-detail",
    ),
    path(
        "tickets/<int:ticket_id>/checkout/",
        TicketCheckoutView.as_view(),
        name="ticket-checkout",
    ),
    path("tickets/entry/",ParkingEntryView.as_view(),name="parking-entry")
]
