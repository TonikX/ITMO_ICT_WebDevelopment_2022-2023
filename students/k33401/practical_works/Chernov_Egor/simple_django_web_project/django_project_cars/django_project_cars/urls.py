from django.urls import path
from cars_first_app import views


urlpatterns = [
    path('', views.index),
    path("driver/<int:id>/", views.get_driver),
]
