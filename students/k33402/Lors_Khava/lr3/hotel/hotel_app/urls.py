from django.urls import path
from .views import *

app_name = "hotel_app"

urlpatterns = [
    path('rooms/', RoomListAPIView.as_view()),
    path('rooms/create/', RoomCreateAPIView.as_view()),
    path('rooms/<int:pk>/', RoomRetrieveAPIView.as_view()),
    path('rooms/update/<int:pk>/', RoomRetrieveUpdateDestroyAPIView.as_view()),
    path('guests/', GuestListAPIView.as_view()),
    path('guests/create/', GuestCreateAPIView.as_view()),
    path('guests/<int:pk>/', GuestRetrieveAPIView.as_view()),
    path('guests/update/<int:pk>/', GuestRetrieveUpdateDestroyAPIView.as_view()),
    path('cleaners/', CleanersListAPIView.as_view()),
    path('cleaners/create/', CleanersCreateAPIView.as_view()),
    path('cleaners/<int:pk>/', CleanersRetrieveAPIView.as_view()),
    path('cleaners/update/<int:pk>/', CleanersRetrieveUpdateDestroyAPIView.as_view()),
    path('cleanings/', CleaningListAPIView.as_view()),
    path('cleanings/create/', CleaningCreateAPIView.as_view()),
    path('bookings/', BookingListAPIView.as_view()),
    path('bookings/<int:pk>/', BookingRetrieveAPIView.as_view()),
    path('bookings/create/', BookingCreateAPIView.as_view()),
    path('bookings/update/<int:pk>/', BookingRetrieveUpdateDestroyAPIView.as_view()),
    path('room/status/', AvailableRoomAPIView.as_view()),
]