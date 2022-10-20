from django.urls import path
from . import views


urlpatterns = [
    path('driver/', views.get_driver),
    path('drivers/', views.get_drivers),
    path('cars/', views.CarList.as_view()),
    path('create_driver/', views.create_driver),
    path('create_car/', views.CarCreate.as_view(success_url="/cars/")),
    path('car/<int:pk>/update', views.CarUpdateView.as_view()),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view()),
]
