from django.urls import path
from django.contrib.auth.views import LoginView
from .views import UserCreateFormView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", UserCreateFormView.as_view(), name="register")
]