from django.urls import path
from .views import FlightListView, FlightDetailView, BookingCreateView, BookingUpdateView, BookingListView

urlpatterns = [
    path("flight_list/", FlightListView.as_view()),
    path("flight_detail/<int:pk>/", FlightDetailView.as_view()),
    path("booking_create/", BookingCreateView.as_view()),
    path("booking_update/<int:pk>/", BookingUpdateView.as_view()),
    path("booking_list/", BookingListView.as_view())
]
