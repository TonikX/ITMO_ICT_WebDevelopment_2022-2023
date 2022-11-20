"""img_rest_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from images.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
      title="API",
      default_version='v2',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kovalev.vxx@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('photos/', PhotoListView.as_view()),
    path('api/colors/', ColorView.as_view()),
    path('api/keywords/', KeywordView.as_view()),
    path('api/search/', SearchPhotoListView.as_view()),
    path("api/likes/create", LikePhotoCreateView.as_view()),
    path("api/likes/<str:pk>", LikePhotoDetailView.as_view()),
    path("api/collections/", CollectionExpandedView.as_view()),
    path("api/collections/create", CollectionCreateView.as_view()),
    path("api/collections/<int:pk>", CollectionDetailView.as_view()),
    path("api/collection-photo/create", CollectionPhotoCreateView.as_view()),
    path("api/collection-photo/<int:pk>", CollectionPhotoDetailView.as_view()),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^api/auth/', include('djoser.urls.authtoken')),
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
