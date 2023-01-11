from django.contrib.auth import views
from django.urls import path

from .views import *

urlpatterns = [
	path('login/', views.LoginView.as_view(), name='login'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	path('register/', register_view, name='register'),
	path('conferences/', conferences_view, name='conferences'),
	path('conferences/<int:pk>', conference_detail, name='conference_detail'),
	path('conferences/<int:pk>/register', conference_register, name='conference_register'),
	path('performances/', performance_view, name='performances'),
	path('performances/<int:pk>', performance_edit, name='performance_edit'),
	path('performances/<int:pk>/delete', performance_delete, name='performance_delete'),
	path('', index_view, name='index'),
]
