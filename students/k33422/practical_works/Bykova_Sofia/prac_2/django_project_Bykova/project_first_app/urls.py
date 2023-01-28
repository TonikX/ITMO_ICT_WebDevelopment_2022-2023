from django.urls import path
from .views import *

urlpatterns = [
    path('owner/<int:id_owner>', info_about_car_owner),
]
