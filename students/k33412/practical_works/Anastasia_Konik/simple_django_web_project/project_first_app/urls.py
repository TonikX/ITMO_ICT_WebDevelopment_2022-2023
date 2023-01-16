from django.urls import path
from .views import *

urlpatterns = [
    path('owner/<int:id>', info_about_car_owner),
    path('owners/', owners),
    path('cars/', CarsList.as_view()),
    path('car/<int:pk>', CarById.as_view()),
    path('create_car_owner/', create_car_owner),
    path('create_car/', CarCreate.as_view()),
    path('update_car/<int:pk>', CarUpdate.as_view()),
    path('delete_car/<int:pk>', CarDelete.as_view()),
]
