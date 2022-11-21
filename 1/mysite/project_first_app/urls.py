from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:pk>/', views.OwnersRetrieveList.as_view()),
    path('owners/', views.OwnersList.as_view(), name="owners"),
    path('car/<int:pk>/', views.CarsRetrieveList.as_view()),
    path('cars/', views.CarsList.as_view(), name="cars"),
    path('own_create/', views.createOwner),
    path('cars/car_create', views.CreateCar.as_view(success_url="/cars/")),
    path('car/<int:pk>/car_delete', views.DeleteCar.as_view()),
    path('car/<int:pk>/car_edit', views.EditCar.as_view())
]
