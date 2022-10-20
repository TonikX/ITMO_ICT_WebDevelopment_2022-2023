from django.urls import include, path
from cars_first_app import views
from django.contrib import admin


urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('', include('cars_first_app.urls')),
]
