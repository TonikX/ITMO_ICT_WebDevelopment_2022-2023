from django.urls import path
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v2',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hardbeat34@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

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

    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
