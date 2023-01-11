from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_index),
    path("owner/<int:id_owner>/", views.get_info_transport_owner),
    path("all_owners/", views.get_all_owners),
    path("all_cars/", views.all_cars.as_view()),
    path("get_car/<int:pk>/", views.get_car_by_id.as_view()),
    path("transport_owner_create", views.create_view),
    path("update_car/<int:pk>/", views.Update_trancpoty.as_view()),
    path("create_car/", views.Create_car.as_view()),
    path("delete_car/<int:pk>/", views.Delete_car.as_view()),
    path("create_new_owner/", views.Create_owner_user.as_view()),
]
