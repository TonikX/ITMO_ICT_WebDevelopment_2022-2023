from django.urls import include, path
from cars_first_app import views


urlpatterns = [
    path('', views.index),
    path('', include('cars_first_app.urls')),
]
