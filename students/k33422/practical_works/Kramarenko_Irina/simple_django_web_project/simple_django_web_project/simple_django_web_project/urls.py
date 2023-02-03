"""django_project_Kramarenko URL Configuration

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
from sproject_first_app import views

urlpatterns = [
    path('owner/<int:owner_id>', views.detail),
    path('admin/', admin.site.urls),
    path('list_owners/', views.list_owners),
    path('list_cars/', views.CarsList.as_view()),
    path('car/<int:pk>/', views.CarByID.as_view()),
    path('update_car/<int:pk>/', views.UpdateCar.as_view()),
    path('create_owner/', views.create_owner),
    path('car/<int:pk>/update/', views.FormUpdateCar.as_view()),
    path('car/create/', views.CreateCar.as_view()),
    path('car/<int:pk>/delete/', views.DeleteCar.as_view()),
]
