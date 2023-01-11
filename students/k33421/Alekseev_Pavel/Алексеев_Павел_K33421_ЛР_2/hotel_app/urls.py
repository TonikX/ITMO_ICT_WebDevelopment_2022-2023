from django.urls import path
from .views import *


urlpatterns = [
    path("guest/list/", guest_list),
    path("guest/create/", guest_create),
    path("room/list/", room_list),
    path("book/", book),
    path("book/list/", book_list),
    path("month/", last_month),
    path("accom/list/", accommodation_list),
    path("accom/<int:pk>/update/", AccomUpdate.as_view()),
    path("accom/<int:pk>/delete/", AccomDelete.as_view()),
    path("home/", home),
    path('hotel/list/', HotelList.as_view()),
    path('hotel/<str:pk>', hotel_view),
    path('hotel/review/<str:pk>', comment)
]

