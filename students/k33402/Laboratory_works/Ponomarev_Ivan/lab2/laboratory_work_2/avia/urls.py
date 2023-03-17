from django.urls import path
from .views import *

urlpatterns = [
    path('', flights, name="flights_url"),
    path('flight/<str:slug>/', get_flight, name="get_flight_url"),
    path('flight/<str:slug>/passengers', get_passengers, name="get_passengers_url"),
    path('book', book, name="book_url"),
    path('reviews', get_reviews, name="get_reviews_url"),
    path('register', register, name="register_url"),
    path('login', login_req, name="login_url"),
    path('logout', logout_req, name="logout_url"),
    path('bookings', get_bookings, name="get_bookings_url"),
    path('bookings/<int:slug>', get_certain_book, name="get_certain_book_url"),
    path('bookings/<int:slug>/delete', delete_certain_book, name='delete_certain_book_url'),
    path('bookings/<int:slug>/review', send_review, name='send_review_url')
]
