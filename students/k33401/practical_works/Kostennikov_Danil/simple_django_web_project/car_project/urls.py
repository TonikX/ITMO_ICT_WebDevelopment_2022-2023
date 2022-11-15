from django.urls import path
from . import views

urlpatterns = [
    path("vehicles", views.VehicleList.as_view()),
]