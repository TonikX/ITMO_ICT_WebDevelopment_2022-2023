from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('auth', views.auth),
    path('logout', views.logout_view),
    path('register', views.registration),
    path('flights', views.flights),
    path('flight/<int:flight_id>/users', views.users_list),
    path('flight/<int:flight_id>/feedbacks', views.feedbacks),
    path('flight/<int:flight_id>/leave_feedback', views.create_feedback),
    path('tickets', views.tickets),
    path('ticket/<int:ticket_id>/delete', views.delete_ticket),
    path('ticket/<int:ticket_id>/update', views.update_ticket),
    path('flight/<int:flight_id>/book', views.book_flight)
]
