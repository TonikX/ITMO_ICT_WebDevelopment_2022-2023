from django.contrib import admin
from django.urls import path, include
from project_first_app import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.owner),
    path('owners_list', views.owners_list),
    path('cars_list', views.CarsList.as_view()),
    path('car/<int:pk>', views.CarsDetail.as_view()),
    path('create_owner', views.create_owner),
    path('car/create', views.CarCreate.as_view()),
    path('car/<int:pk>/update', views.CarUpdate.as_view()),
    path('car/<int:pk>/delete', views.CarDelete.as_view()),
]
