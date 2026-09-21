from django.urls import path

from .views import TicketListCreateView, TicketDetailView


urlpatterns = [
    path('tickets/',TicketListCreateView.as_view(),name="ticket_list_create"),
    path('tickets/<int:ticket_id>/',TicketDetailView.as_view(),name="ticket_detail")
]
