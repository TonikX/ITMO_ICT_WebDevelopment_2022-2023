
from django.contrib import admin
from django.urls import path
from hotels.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
path('main/', main_page, name='main_page'),
    path("guests/add/", AddGuests.as_view(), name='add_guest'),
    path('guests/<str:hotel_name>', guests_list),
    path("rooms/", ListRooms.as_view(), name='rooms'),
    path("bookings/create", CreateBooking.as_view(), name='add_booking'),
    path("bookings/my/", MyBookings, name='my_bookings'),
    path("bookings/<int:guest_passport>/", UserBookings),
    path("bookings/update/<int:pk>", UpdateBooking.as_view()),
    path("bookings/delete/<int:pk>", DeleteBooking.as_view()),
    path("feedbacks/add/", AddFeedback, name='give_feedback'),
    path('feedbacks/',AllFeedbacks, name='all_feedbacks'),
    path('hotel/', get_hotel, name='hotel'),
]
