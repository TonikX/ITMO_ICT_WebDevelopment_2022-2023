from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('signup/', views.SignUp.as_view(), name="sign_up"),
    path('login/', views.LogIn.as_view(), name="log_in"),
    path('logout/', views.LogOut.as_view(), name="log_out"),
    path('profile/', views.Profile.as_view(), name="profile"),
    path('flights/', views.Flights.as_view(), name="flights"),
]
