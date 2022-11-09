from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path("", views.HotelList.as_view(), name="hotels"),
    path("hotel/<int:pk>", views.HotelInfo.as_view(), name="hotel_info"),
    path("room/<int:pk>", views.RoomInfo.as_view(), name="room_info"),
    path("room/<int:pk>/reserve", login_required(views.reserve_room, login_url="login"), name="reserve"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
]
