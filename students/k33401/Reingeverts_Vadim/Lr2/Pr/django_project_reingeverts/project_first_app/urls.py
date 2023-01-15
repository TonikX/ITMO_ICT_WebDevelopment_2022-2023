from django.urls import path

from . import views

urlpatterns = [
    path('car-owner/<int:car_owner_pk>',
         views.car_owner_detail, name='car-owner-detail'),
    path('ownership/<int:ownership_pk>',
         views.ownership_detail, name='ownership-detail'),
]
