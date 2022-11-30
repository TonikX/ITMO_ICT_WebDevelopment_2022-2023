from django.contrib import admin
from django.urls import path, include
from practical import views
from practical.views import *



urlpatterns = [
    path('owners/', views.all_owners_detail),
    path('owner/<int:owner_id>/', views.owner_detail),
    path('create_owner/', views.create_owner),
    path('cars/', AllCars.as_view()),
    path('car/<int:pk>/', OneCar.as_view()),
    path('car/<int:pk>/update/', CarUpdate.as_view()),
    path('car/create/', CarCreate.as_view()),
    path('car/<int:pk>/delete/', CarDelete.as_view()),
]