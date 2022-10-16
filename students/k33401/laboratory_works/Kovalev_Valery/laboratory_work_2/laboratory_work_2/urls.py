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
    path("add_info/", timetable.views.add_info, name="add_info"),
    path("logout/", timetable.views.logoutUser, name="logout"),
    path("marks/", timetable.views.marks, name="marks"),
    path("teacher_marks/", timetable.views.teacher_marks_page, name="teacher_marks"),
    path("student_marks/", timetable.views.student_marks_page, name="student_marks"),
    path("make_homework/<int:work_id>/", timetable.views.make_homework, name="make_homework"),
    path("create_homework/<int:work_id>/", timetable.views.create_homework, name="create_homework")
]
