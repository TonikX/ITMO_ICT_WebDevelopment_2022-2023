from django.urls import path
from . import views

urlpatterns = [
    path('owners', views.get_owners),
    path('cars', views.Car_view.as_view()),
    path('owner/add', views.add_owner),
    path('car/<int:pk>/update', views.CarUpdate.as_view()),
    path('car/create', views.CarCreate.as_view()),
    path('car/<int:pk>/delete', views.CarDelete.as_view()),
]