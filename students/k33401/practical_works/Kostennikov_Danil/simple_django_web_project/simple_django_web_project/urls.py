"""simple_django_web_project URL Configuration

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
from django.urls import path, include
from car_project import views

urlpatterns = [
    path('admin/', admin.site.urls),
 #   path('', include('car_project'))
    path("cars", views.CarList.as_view()),
    path("cars/create", views.CarCreate.as_view(success_url="/cars")),
    path("cars/update/<int:pk>", views.CarUpdate.as_view()),
    path("cars/delete/<int:pk>", views.CarDelete.as_view()),
    path("owner/create", views.create_owner),
    path("owners",views.owners),
    path("owners/<int:id>/", views.owner)
]
