from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import ConferencesList, CustomLoginView, RegisterPage, ThemesList, ThemeDetail, conference_detail, conference_register_view, RegisterList, DeleteRegisterView

urlpatterns = [
    path('', ConferencesList.as_view(), name='conferences'),
    path('conference/<int:pk>', conference_detail,
         name='conference'),
    path('conference/<int:pk>/register',
         conference_register_view, name='conference_register'),
    path('myregisters',
         RegisterList.as_view(), name='my_registers'),
    path('myregisters/delete/<int:pk>',
         DeleteRegisterView.as_view(), name='register_delete'),
    path('themes', ThemesList.as_view(), name='themes'),
    path('themes/<int:pk>', ThemeDetail.as_view(), name='theme'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='conferences'), name='logout'),
    path('register', RegisterPage.as_view(), name='register'),
]
