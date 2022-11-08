from django.urls import path
from . import views

urlpatterns = [
    path("", views.HotelList.as_view(), name="hotels"),
    path("hotel/<int:pk>", views.hotel_info, name="hotel_info")
]
