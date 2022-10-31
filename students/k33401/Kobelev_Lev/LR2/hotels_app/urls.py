from django.urls import path
from .views import *

urlpatterns = [
    # hotels and rooms
    path('hotel/list/', HotelListView.as_view()),
    path('hotel/<hotel_id>/rooms', get_hotel_rooms),
    path('hotel/<hotel_id>/rooms/<room_number>', get_room, name="get_room"),

    # bookings
    path('bookings/', get_bookings),
    path('bookings/<int:pk>/delete/', BookingDeleteView.as_view()),
    path('bookings/<int:pk>/update/', BookingUpdateView.as_view()),
]