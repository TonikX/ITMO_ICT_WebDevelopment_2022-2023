from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegView.as_view(), name='index'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('hotels/', views.HotelListView.as_view(), name='hotels'),
    path('hotels/<int:pk>/', views.HotelView.as_view(), name='hotel'),
    path('hotels/<int:id_hotel>/<int:id_rt>/rooms/', views.RoomListView.as_view(), name='hotel-rooms'),
    path('hotels/<int:id_hotel>/<int:id_rt>/rooms/<int:pk>', views.RoomView.as_view(), name='room'),
]

# Просмотр отелей и номеров
# hotels/
# hotels/<int:pk>
# hotels/<int:pk>/room_types/
# hotels/<int:pk>/room_types/<int:pk>
# hotels/<int:pk>/room_types/<int:pk>/rooms/
# hotels/<int:pk>/room_types/<int:pk>/rooms/<int:pk>

# Вход/рег
# account/login/
# account/registration/

# Личный акк
# account/user/<int:id>

# Написание отзыва
# hotels/<int:id>/rooms/<int:id>/review

# username: test1
# mail: test1@mail.ru
# password: test12344321