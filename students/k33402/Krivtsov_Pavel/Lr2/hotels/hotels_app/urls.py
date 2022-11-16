from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path("", views.HotelList.as_view(), name="hotels"),
    path("hotel/<int:pk>", views.HotelInfo.as_view(), name="hotel_info"),
    path("room/<int:pk>", views.room_info, name="room_info"),
    path("room/<int:pk>/reserve", login_required(views.ReservationView.reserve_room, login_url="login"), name="reserve"),
    path("reservation/<int:pk>/update",
         login_required(views.ReservationView.update_reservation, login_url="login"),
         name="update_reservation"),
    path("reservation/<int:pk>/delete",
         login_required(views.ReservationView.delete_reservation, login_url="login"),
         name="delete_reservation"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", login_required(views.profile, login_url="login"), name="profile"),
]
