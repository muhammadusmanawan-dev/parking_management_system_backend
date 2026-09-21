from django.urls import path

from .views import TicketListCreateView


urlpatterns = [
    path('tickets/',TicketListCreateView.as_view(),name="ticket_list_create"),
]
