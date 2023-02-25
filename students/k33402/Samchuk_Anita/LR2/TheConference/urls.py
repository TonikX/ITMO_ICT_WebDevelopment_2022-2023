from django.urls import path
from django.contrib.auth import views

from .views import *

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login_url'),
    path('logout', views.LogoutView.as_view(), name='logout_url'),
    path('registration', user_registration, name='user_registration_url'),
    path('', conf_list, name='conf_list_url'),
    path('conf/<str:name>/', conf_registration, name='conf_registration_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:title>', tags_detail, name='tags_detail_url'),
    path('account', account, name='account_url')
]
