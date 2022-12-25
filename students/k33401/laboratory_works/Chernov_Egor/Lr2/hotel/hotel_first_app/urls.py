from django.urls import path
from .views import *


urlpatterns = [
    path('hotels/', HotelListView.as_view(), name='hotels'),
    path('hotels/<int:pk>/', HotelView.as_view(), name='hotel'),
    path('hotels/<int:id_hotel>/<int:id_rt>/rooms/', RoomListView.as_view(), name='hotel-rooms'),
    path('hotels/<int:id_hotel>/<int:id_rt>/rooms/<int:pk>/', RoomView.as_view(), name='room'),
    path('hotels/<int:id_hotel>/<int:id_rt>/rooms/<int:id_room>/comment/', CommentView.as_view(), name='comment'),
    path('reserve/', ReserveView.as_view(), name='reserve'),
    path('hotels/<int:id_hotel>/<int:id_rt>/rooms/<int:id_room>/reserve/', ReserveRoomView.as_view(), name='reserve-room'),
]
