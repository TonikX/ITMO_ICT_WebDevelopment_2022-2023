from django.urls import path
from . import views

urlpatterns = [
    path("", views.HotelList.as_view(), name="hotels"),
    path("hotel/<int:pk>", views.HotelInfo.as_view(), name="hotel_info"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("register/", views.RegisterUser.as_view(), name="register"),
]
