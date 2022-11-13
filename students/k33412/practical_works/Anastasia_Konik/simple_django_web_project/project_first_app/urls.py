from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:id>', views.info_about_car_owner)
]