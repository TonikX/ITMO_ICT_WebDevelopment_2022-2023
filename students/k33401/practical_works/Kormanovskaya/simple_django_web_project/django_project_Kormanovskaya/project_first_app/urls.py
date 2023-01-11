from django.urls import path
from . import views

urlpatterns = [
    path("drivers/<int:driver_id>", views.driver),
    path("drivers/", views.drivers),
    path("drivers/create", views.create_driver),

    path("vehicles", views.VehicleList.as_view()),
    path('vehicles/<int:pk>/update/', views.VehicleUpdate.as_view()),
    path('vehicles/create', views.VehicleCreate.as_view(success_url="/vehicles")),
    path('vehicles/<int:pk>/delete/', views.VehicleDelete.as_view()),
]
