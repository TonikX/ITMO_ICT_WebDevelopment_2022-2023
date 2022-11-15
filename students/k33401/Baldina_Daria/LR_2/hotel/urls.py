from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main_page, name = 'main_page'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', Logout.as_view(), name = 'logout'),
    path("rooms/", RoomsList.as_view(),  name = 'rooms'),
    path("book/",  BookingCreateView.as_view(),  name = 'book'),
    path("users_bookings/", user_book, name = 'my_bookings'),
    path("update_book/<int:pk>", UpdateBooking.as_view()),
    path("del_book/<int:pk>", DeleteBooking.as_view()),
    path("comment/", CommentCreateView.as_view(), name = 'comment'),
    path('all_comments/', all_comments, name = 'all_comments'),
    path('hotel/', guests_list, name = 'hotel_info'),
]