from django.urls import path
from .views import *


urlpatterns = [
    path('hotels/', HotelListView.as_view(), name='hotels'),
    path('hotels/<int:pk>/', HotelView.as_view(), name='hotel'),
    path('hotels/<int:id_hotel>/<int:id_rt>/rooms/', RoomListView.as_view(), name='hotel-rooms'),
    path('hotels/<int:id_hotel>/<int:id_rt>/rooms/<int:pk>/', RoomView.as_view(), name='room'),
    path('hotels/<int:id_hotel>/<int:id_rt>/rooms/<int:id_room>/comment/', CommentView.as_view(), name='comment'),
]

# Просмотр отелей и номеров
# hotels/
# hotels/<int:pk>
# hotels/<int:pk>/room_types/
# hotels/<int:pk>/room_types/<int:pk>
# hotels/<int:pk>/room_types/<int:pk>/rooms/
# hotels/<int:pk>/room_types/<int:pk>/rooms/<int:pk>

# Написание отзыва
# hotels/<int:id>/rooms/<int:id>/review

# username: test1
# mail: test1@mail.ru
# password: test12344321
