from django.urls import path
from . import views

urlpatterns = [
    path("owner/<int:id_owner>/", views.get_info_transport_owner),
    path('get_all_owners/', views.get_all_owners),
    path('get_all_cars/', views.get_all_cars),
    path("update_car_info/<int:pk>/", views.update_car_info.as_view()),
    path("get_car_by_id/<int:pk>/", views.get_car_by_id.as_view()),
    path("create_new_owner/", views.create_new_owner.as_view()),
    path("create_new_car/", views.create_new_car.as_view()),
    path("<int:pk>/delete_car/", views.delete_car.as_view()),

]
