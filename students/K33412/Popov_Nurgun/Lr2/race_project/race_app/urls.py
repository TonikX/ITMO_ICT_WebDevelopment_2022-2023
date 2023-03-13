from django.urls import path
from . import views
#from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('login', views.loginPage),
    path('register', views.reg_page),
    path('logout', views.logoutUser),
    path('races/', views.races, name='races'),
    path('race/<int:pk>/comment', views.writeComment, name="comment"),
    path('race/<int:pk>/registrate', views.raceReg, name="race_reg"),
    path('race/<int:pk>/delete', views.deleteReg, name='delete'),
    path('race/<int:pk>/edit', views.changeRace, name="race_edit"),
    path('race/<int:pk>/results', views.results, name="results"),
    path('race/<int:pk>/change_reg', views.changeReg, name="registration_ch"),
]