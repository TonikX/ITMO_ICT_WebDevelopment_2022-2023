"""django_project_borsov_2_2 URL Configuration

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
from project_first_app.views import car_info, car_info_full, create_new_owner
from project_first_app.views import CarsRetrieveView, CarRetrieveView, CarUpdateView, CarCreateView, CarDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('owner/<int:car_id>', car_info),
    path('owners/<int:car_id>', car_info_full),
    path('carsInfo/', CarsRetrieveView.as_view()),
    path('carInfo/<int:pk>', CarRetrieveView.as_view()),
    path('carInfo/create', CarCreateView.as_view()),
    path('carInfo/<int:pk>/update', CarUpdateView.as_view()),
    path('carInfo/<int:pk>/delete', CarDeleteView.as_view()),
    path('createOwner', create_new_owner)
]
