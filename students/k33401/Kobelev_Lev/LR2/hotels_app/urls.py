from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    # hotels and rooms
    path('hotel/list/', HotelListView.as_view()),
    path('hotel/<int:pk>/', HotelDetailView.as_view()),
    path('hotel/<hotel_id>/<int:pk>/', RoomDetailView.as_view(), name="get_room"),

    # bookings
    path('bookings/', login_required(BookingListView.as_view()), name="bookings"),
    path('bookings/<int:pk>/delete/', login_required(BookingDeleteView.as_view())),
    path('bookings/<int:pk>/update/', login_required(BookingUpdateView.as_view())),
]