from django.urls import path
from .views import PaymentDetailView, PaymentListCreateView, PaymentStatusView

urlpatterns = [
    path("payments/", PaymentListCreateView.as_view(), name="payment-list-create"),
    path(
        "payments/<int:payment_id>/", PaymentDetailView.as_view(), name="payment-detail"
    ),
    path(
        "payments/<int:payment_id>/status/",
        PaymentStatusView.as_view(),
        name="payment-status",
    ),
]
