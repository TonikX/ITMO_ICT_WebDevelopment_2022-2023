from django.urls import path 
from . import views

urlpatterns = [
    path('owner/<int:car_owner_id>/', views.car_owner_info),
    path('all_owners/', views.all_owners),
    path('owner/create/', views.car_owner_create),
    path('all_cars/', views.AllCars.as_view()),
    path('car/<int:pk>/', views.CarInfo.as_view()),
    path('car/<int:pk>/update/', views.CarUpdate.as_view()),
    path('car/create/', views.CarCreate.as_view()),
    path('car/<int:pk>/delete/', views.CarDelete.as_view()),
]