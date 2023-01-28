from django.urls import path
from django.views.generic import TemplateView
from .views import TourListView, ReservationListView, TourAndReviewsView, CreateReservationView, CreateReviewView

urlpatterns = [
    path("", TemplateView.as_view(template_name="tours/index.html"), name="index"),
    path("tours/", TourListView.as_view(), name="tours"),
    path("reservations/", ReservationListView.as_view(), name="reservations"),
    path("tours/<int:pk>/", TourAndReviewsView.as_view(), name="reviews"),
    path("reserve/", CreateReservationView.as_view(), name="reserve"),
    path("write/", CreateReviewView.as_view(), name="write")
]