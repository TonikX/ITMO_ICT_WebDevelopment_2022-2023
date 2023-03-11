from django.urls import path
from .views import *

urlpatterns = [
    path("home/", home),
    path("client_list/", clients_list),
    path("client_create/", clients_create),
    path("room_list/", room_list),
    path("book/", book),
    path("book_list/", book_list),
    path("month/", last_month),
    path("book_update/<int:pk>/", BookUpdate.as_view()),
    path("book_delete/<int:pk>/", BookDelete.as_view()),
    path('hotel_list/', HotelList.as_view()),
    path('hotel/<str:pk>', hotel_view),
    path('hotel/review/<str:pk>', comment)
]