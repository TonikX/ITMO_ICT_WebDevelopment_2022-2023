"""Desk URL Configuration

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
from django.contrib import admin
from django.urls import path
import table.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', table.views.registerPage, name="register"),
    path('login/', table.views.loginPage, name="login"),
    path("", table.views.home, name="home"),
    path("add_info/", table.views.add_info, name="add_info"),
    path("logout/", table.views.logoutUser, name="logout"),
    path("marks/", table.views.marks, name="marks"),
    path("teacher_marks/", table.views.teacher_marks_page, name="teacher_marks"),
    path("student_marks/", table.views.student_marks_page, name="student_marks"),
    path("make_homework/<int:work_id>/", table.views.make_homework, name="make_homework"),
    path("change_homework/<int:work_id>/", table.views.change_homework, name="change_homework"),
    path("create_homework/", table.views.create_homework, name="create_homework"),
    path("teacher_home/", table.views.teacher_home_page, name="teacher_home"),
    path("student_home/", table.views.student_home_page, name="student_home"),
    path("delete_homework/<int:work_id>/", table.views.delete_homework, name="delete_homework"),
    path("rate_homework/<int:work_id>/", table.views.rate_homework, name="rate_homework")
]
