"""Cars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
#from cars_app.views import *
import cars_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('owner/<int:id_owner>', cars_app.views.info_about_car_owner),
    path('list_owners/', cars_app.views.all_owners),
    path('list_cars/', cars_app.views.CarList.as_view()),
    path('car/<int:pk>', cars_app.views.CarById.as_view()),
    path('create_owner/', cars_app.views.create_owner),
    path('update_car/<int:pk>', cars_app.views.CarUpdate.as_view()),
    path('create_car/', cars_app.views.CarCreate.as_view()),
    path('delete_car/<int:pk>', cars_app.views.CarDelete.as_view()),
]
