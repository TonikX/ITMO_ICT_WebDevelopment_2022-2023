from django.urls import path
from .views import *

urlpatterns = [
    # hotels and rooms
    path('hotel/list/', HotelListView.as_view()),
    path('hotel/<int:pk>/', HotelDetailView.as_view()),
    path('hotel/<hotel_id>/<room_number>', get_room, name="get_room"),

    # bookings
    path('bookings/', BookingListView.as_view()),
    path('bookings/<int:pk>/delete/', BookingDeleteView.as_view()),
    path('bookings/<int:pk>/update/', BookingUpdateView.as_view()),
]