from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main_page, name = 'main_page'),
    path("registration/", RegGuests.as_view(), name = 'reg'),
    path("rooms/", RoomsList.as_view(),  name = 'rooms'),
    path("book/", create_reservation,  name = 'book'),
    path("my_bookings/", my_bookings, name = 'my_bookings'),
    path("users_bookings/<int:guest_passport>/", user_book),
    path("update_book/<int:pk>", UpdateBooking.as_view()),
    path("del_book/<int:pk>", DeleteBooking.as_view()),
    path("comment/", create_comment, name = 'comment'),
    path('all_comments/', all_comments, name = 'all_comments'),
    path('hotel/', get_hotel, name = 'hotel_info'),
    path('guests/<str:hotel_name>', guests_list)
]