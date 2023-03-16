from django.urls import path 
from .views import *
urlpatterns = [
    path('', FlightsList.as_view()),
    path('register/', UserRegister.as_view()),
    path('login/', LoginUser.as_view()),
    path('logout/', logout_user),
    path('book/<id_flight>', book_flight),
    path('my_bookings/', BookingsList.as_view()),
    path('my_bookings/<int:pk>/update/', BookingUpdate.as_view()),
    path('my_bookings/<int:pk>/delete/', BookingDelete.as_view()),
    path('passengers/<id_flight>', PassengersList.as_view()),
    path('reviews', ReviewsList.as_view()),
    path('reviews/create/', review_create),
]