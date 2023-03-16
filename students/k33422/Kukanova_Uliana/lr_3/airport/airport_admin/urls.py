from django.urls import path
from .views import *

urlpatterns = [
    path('employees/', EmployeeListView.as_view()),
    path('employees/create/', EmployeeCreateView.as_view()),
    path('employees/<int:pk>/', EmployeeModifyView.as_view()),
    path('airplanes/', AirplaneListView.as_view()),
    path('airplanes/create/', AirplaneCreateView.as_view()),
    path('airplanes/<int:pk>/', AirplaneModifyView.as_view()),
    path('schedule/', ScheduleListView.as_view()),
    path('schedule/create/', ScheduleCreateView.as_view()),
    path('schedule/<int:pk>/', ScheduleModifyView.as_view()),
    path('flights/', FlightListView.as_view()),
    path('flights/create/', FlightCreateView.as_view()),
    path('flights/<int:pk>/', FlightModifyView.as_view()),
    path('airline_admin/', AirlineAdministrationListView.as_view()),
    path('airline_admin/create/', AirlineAdministrationCreateView.as_view()),
    path('airline_admin/<int:pk>/', AirlineAdministrationModifyView.as_view()),
    path('transit/', TransitListView.as_view()),
    path('transit/create/', TransitCreateView.as_view()),
    path('transit/<int:pk>/', TransitModifyView.as_view())
]
