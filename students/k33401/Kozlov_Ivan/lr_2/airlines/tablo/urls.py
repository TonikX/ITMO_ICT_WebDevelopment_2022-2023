from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("registration/", views.Reg_user.as_view(), name="reg_users"),
    path("", views.get_main_title, name="index"),
    path("admin/", admin.site.urls),
    path("book/", views.Book.as_view(), name="book"),
    path("trip/", views.Trip.as_view(), name="trip"),
    path("current_book/<int:passport_user>/", views.get_current_book, name="current_book"),
    path("choose_passport_for_book/", views.my_book, name="choose_passport_for_book"),
    path("up_ticket/<int:pk>", views.Update_ticket.as_view(), name="update_ticket"),
    path("del_ticket/<int:pk>", views.Delete_ticket.as_view(), name="delete_ticket"),
    path("all_passangers/<int:flight_num>", views.all_passengers, name="all_passangers"),
    path("create_review/", views.Create_review.as_view(), name="create_review"),
    path("review/", views.All_reviews.as_view(), name="reviews"),
]
