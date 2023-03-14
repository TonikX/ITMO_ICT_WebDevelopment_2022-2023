"""HotelBorsovProject URL Configuration

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
from django.urls import path
from hotel import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name="main_page"),
    path("register", views.register_request, name='registartion'),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("room/<int:pk>", views.room, name='room'),
    path("guests_table", views.guests_table, name='guests_table'),
    path("mybooking", views.my_booking, name='mybooking'),
    path("booking/<int:pk>/delete", views.delete_my_booking, name='booking_delete'),
    path("booking/<int:pk>/edit", views.edit_my_booking, name='booking_edit'),

]
