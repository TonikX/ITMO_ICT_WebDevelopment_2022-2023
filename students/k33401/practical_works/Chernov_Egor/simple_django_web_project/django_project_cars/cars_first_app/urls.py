from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('driver/<int:id>/', get_driver),
    path('drivers/', get_drivers),
    path('cars/', CarList.as_view()),
    path('create_driver/', create_driver),
    path('create_car/', CarCreate.as_view(success_url="/cars/")),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),

    path('api/drivers/', DriverAPIView.as_view()),
    path('api/driver/create/', CreateDriverAPIView.as_view()),
    path('api/drivers_with_license/', DriverAndLicenseAPIView.as_view()),
    path('api/driver/<int:pk>/', RetrieveDriverAPIView.as_view()),
    path('api/driver/<int:pk>/update_or_delete/', RetrieveDriverUpdateDestroyAPIView.as_view()),
]
