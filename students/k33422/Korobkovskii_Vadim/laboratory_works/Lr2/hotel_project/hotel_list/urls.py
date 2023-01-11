from django.urls import path
from .views import *

urlpatterns = [
    path('', Homepage.as_view()),
    path('start/', Homepage.as_view()),
    path('register/', register, name='register'),
    path('login/', login_, name='login'),
    path('logout/', logout_, name='logout'),

    path('main_page/', IndexView.as_view(), name='main_page'),
    path('hotels/', HotelList.as_view(), name='hotel_list'),
    path('hotels/<str:pk>', HotelRetrieveView.as_view()),

    path('reservations/', ListReservation.as_view(), name='my_reservation'),
    path('reservations/create/', create_reservation, name='reservation'),
    path('reservations/<str:pk>', ReservationRetrieveView.as_view()),
    path('reservations/<str:pk>/update/', ReservationUpdateView.as_view(success_url='/reservations/')),
    path('reservations/<int:pk>/delete/', ReservationDeleteView.as_view(success_url='/reservations/')),
    path('reservations/<int:pk>/review/', ReviewCreateView.as_view(success_url='/reservations/')),

    path('rooms/', ListRoom.as_view(), name='room_list'),
    path('rooms/<str:pk>', RoomRetrieveView.as_view()),

    path('reviews/', ReviewList.as_view(), name='review'),
    path('reviews/<str:pk>', ReviewRetrieveView.as_view()),
    path('my_reviews/', MyReviewList.as_view(), name="my_review"),
    path('reviews/<str:pk>', ReviewRetrieveView.as_view()),
    path('reviews/<str:pk>/update/', ReviewUpdateView.as_view()),
    path('reviews/<str:pk>/delete/', ReviewDeleteView.as_view()),

    path('guests/', GuestsList.as_view(), name='guests'),
    ]
