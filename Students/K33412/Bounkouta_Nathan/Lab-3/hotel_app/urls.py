from django.urls import path
from .views import *

app_name = "hotel_app"

urlpatterns = [
    path('rooms/', RoomListAPIView.as_view()),
    path('rooms/create/', RoomCreateAPIView.as_view()),
    path('rooms/<int:pk>/', RoomRetrieveAPIView.as_view()),
    path('rooms/update/<int:pk>/', RoomRetrieveUpdateDestroyAPIView.as_view()),
    path('clients/', ClientListAPIView.as_view()),
    path('clients/create/', ClientCreateAPIView.as_view()),
    path('clients/<int:pk>/', ClientRetrieveAPIView.as_view()),
    path('clients/update/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view()),
    path('employees/', EmployeeListAPIView.as_view()),
    path('employees/create/', EmployeeCreateAPIView.as_view()),
    path('employees/<int:pk>/', EmployeeRetrieveAPIView.as_view()),
    path('employees/update/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view()),
    path('bookings/', BookingListAPIView.as_view()),
    path('bookings/create/', BookingCreateAPIView.as_view()),
]