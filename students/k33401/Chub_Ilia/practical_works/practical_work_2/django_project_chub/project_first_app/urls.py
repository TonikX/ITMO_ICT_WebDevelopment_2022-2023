from .views import *
from django.urls import path

cars_owners_urls = [
    path('cars_owners/<int:owner_id>', get_car_owner_info),
    path('cars_owners/all', get_cars_owners_list),
    path('cars_owners/create', create_car_owner)
]

cars_urls = [
    path('cars/create', CreateCarInfo.as_view()),
    path('cars/update/<int:pk>', UpdateCarInfo.as_view()),
    path('cars/delete/<int:pk>', DeleteCarInfo.as_view()),
    path('cars/<int:pk>', GetCarInfo.as_view()),
    path('cars/all', GetCarsList.as_view())
]

urlpatterns = (
    []
    + cars_urls
    + cars_owners_urls
)
