from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistrationView

# Список URL приложения авторизации
urlpatterns = [
    path("login/", LoginView.as_view(next_page="/", template_name="auth/login.html")),
    path("logout/", LogoutView.as_view(next_page="/")),
    path("registration/", RegistrationView.as_view())
]
