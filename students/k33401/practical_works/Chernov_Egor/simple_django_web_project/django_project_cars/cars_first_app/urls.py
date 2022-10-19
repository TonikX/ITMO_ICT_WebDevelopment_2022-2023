from django.urls import path
from . import views


urlpatterns = [
    path("driver/<int:id>/", views.get_driver),
]
