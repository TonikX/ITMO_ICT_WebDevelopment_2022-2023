from django.urls import path

from .views import *

urlpatterns = [
    path('flights/', flights_list, name='flights_list_url'),
    path('flights/<str:slug>/', flight_details, name='flight_details_url'),

    path('registration/', registration, name='registration_url'),
    path('login/', login_page, name='login_url'),
    path('logout/', logout_user, name='logout_url'),

    path('profile/', profile, name='profile_url'),
    path('profile/ticket/<int:pk>/delete/', ticket_delete, name='ticket_delete_url'),
    path('profile/ticket/<int:pk>/review/update/', ReviewUpdate.as_view()),
    path('profile/ticket/<int:pk>/update/', TicketUpdate.as_view()),
]
