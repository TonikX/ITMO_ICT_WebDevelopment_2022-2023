"""laboratory_work_2 URL Configuration

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

import timetable.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', timetable.views.registerPage, name="register"),
    path('login/', timetable.views.loginPage, name="login"),
    path("", timetable.views.home, name="home"),
    path("teacher/", timetable.views.for_student, name="student"),
    path("add_info/", timetable.views.add_info, name="add_info")
]
