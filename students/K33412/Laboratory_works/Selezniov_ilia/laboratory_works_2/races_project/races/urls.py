from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('', views.races),
    path('races/<int:pk_test>/drivers', views.drivers, name="race"),
    path('races/', views.races, name="races"),
    path('home/', views.home, name="home"),
    path('registration/create', views.createReg, name="registration_cr"),
    path('registration/<int:pk>/change', views.changeReg, name="registration_ch"),
    path('registration/<int:pk>/delete', views.deleteReg, name="registration_dl"),
    path('car/create', views.createCar, name="car_cr"),
    path('car/<int:pk>/change', views.changeCar, name="car_ch"),
    path('register', views.regPage, name="register"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('driver_cr', views.regDriver, name="driver_cr"),
    path('race/<int:pk>/registrate', views.raceReg, name="race_reg"),
    path('race/<int:pk>/comment', views.writeComment, name="comment"),
    path('race/create', views.createRace, name="race_cr"),
    path('race/<int:pk>/change', views.changeRace, name="race_ch"),
    path('race/<int:pk>/results', views.results, name="results"),
    path('race/<int:pk>/comments', views.comments, name="comments"),
    path('race/<int:pk>/delete', views.delRace, name="race_dl"),
]
