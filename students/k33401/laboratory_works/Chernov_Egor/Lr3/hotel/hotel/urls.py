from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="Description:",
        terms_of_service="https://drive.google.com/file/d/1QxQo5jln6soFUj6EmOVEo1yauCo375PP/view",
        contact=openapi.Contact(email="krish19poroh@mail.ru"),
        license=openapi.License(name="API for the project \"Hotel\""),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include('hotel_app.urls')),
]
