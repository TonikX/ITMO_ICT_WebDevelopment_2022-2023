from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('auth', views.auth),
    path('logout', views.logout_view),
    path('signup', views.register_request),
    path('table', views.FlightList.as_view()),
    path('flight/<int:flight_id>/order', views.order),
    path('flight/<str:flight_number>/review/create', views.review),
    path('flight/<str:flight_number>/review', views.reviews),
    path('flight/<str:flight_number>/passenger', views.passengers),
    path('ticket', views.tickets),
    path('ticket/<int:pk>/delete', views.TicketDelete.as_view()),
    path('ticket/<int:pk>/update', views.TicketUpdate.as_view()),
]