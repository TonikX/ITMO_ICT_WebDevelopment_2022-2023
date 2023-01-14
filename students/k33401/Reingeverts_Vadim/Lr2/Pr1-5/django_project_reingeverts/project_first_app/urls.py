from django.urls import path

from . import views

urlpatterns = [
    path('owner/<int:car_owner_pk>',
         views.car_owner_detail, name='car-owner-detail'),
]
