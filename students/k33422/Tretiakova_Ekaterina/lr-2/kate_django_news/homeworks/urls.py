from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add-user', views.create_user),
    path('add-subject', views.create_subject),
    path('add-homework', views.create_homework),
    path('add-grade', views.create_grade),
    ]