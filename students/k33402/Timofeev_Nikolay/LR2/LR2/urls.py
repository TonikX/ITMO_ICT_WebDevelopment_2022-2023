from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib import admin
from megaultrabooking.views import (
    hotels_list,
    rooms_list,
    reviews_list,
    register_user,
    add_hotel,
    add_room,
    add_review,
    add_booking,
    bookings_list,
    personal_page,
    edit_booking,
    hotel_statistics,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("personal/", personal_page, name="personal"),
    path("register/", register_user, name="register"),
    path("hotels/", hotels_list, name="hotels_list"),
    path("hotels/add", add_hotel, name="add_hotel"),
    path("hotels/<int:hotel_id>/statistics/", hotel_statistics, name="hotel_statistics"),
    path("hotels/<int:hotel_id>/rooms/", rooms_list, name="rooms_list"),
    path("hotels/<int:hotel_id>/rooms/add", add_room, name="add_room"),
    path("hotels/<int:hotel_id>/rooms/<int:room_id>/reviews/", reviews_list, name="reviews_list"),
    path("hotels/<int:hotel_id>/rooms/<int:room_id>/booking/", add_booking, name="add_booking"),
    path("bookings/<int:booking_id>", bookings_list, name="bookings_list"),
    path("bookings/<int:booking_id>/review", add_review, name="add_review"),
    path("bookings/<int:booking_id>/edit", edit_booking, name="edit_booking"),
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
]
