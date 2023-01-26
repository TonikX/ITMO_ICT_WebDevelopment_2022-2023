from django.urls import path
from .views import *

urlpatterns = [
    path('passengers/all', PassengerListView.as_view()),
    path('passengers/create/', PassengerCreateView.as_view()),
    path('passengers/<int:pk>/', PassengerEditView.as_view()),
    path('planes/all', PlaneListView.as_view()),
    path('planes/create/', PlaneCreateView.as_view()),
    path('planes/<int:pk>/', PlaneEditView.as_view()),
    path('flights/all', FlightListView.as_view()),
    path('flights/create/', FlightCreateView.as_view()),
    path('flights/<int:pk>/', FlightEditView.as_view()),
    path('airlines/all', AirCompanyListView.as_view()),
    path('airlines/create/', AirCompanyCreateView.as_view()),
    path('airlines/<int:pk>/', AirCompanyEditView.as_view()),
    path('tickets/all', TicketListView.as_view()),
    path('tickets/create/', TicketCreateView.as_view()),
    path('tickets/<int:pk>/', TicketEditView.as_view())
]