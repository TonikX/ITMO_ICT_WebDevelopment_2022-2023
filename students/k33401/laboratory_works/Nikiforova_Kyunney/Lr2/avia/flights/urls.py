from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('registration/', views.user_registration, name='register'),
    path('flight_list/', views.FlightList.as_view(), name='flight_list'),
    path('booking/', views.create_booking, name='booking'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('passenger_bookings/<int:passport>/', views.passenger_bookings),
    path('bookings/<int:pk>/update', views.TicketUpdate.as_view()),
    path('bookings/<int:pk>/delete', views.TicketDelete.as_view()),
    path('all_passengers/<str:flight_number>', views.all_passengers),
    path('all_comments/', views.all_comments, name='all_comments'),
    path('create_comment/', views.create_comment, name='create_comment'),
]
