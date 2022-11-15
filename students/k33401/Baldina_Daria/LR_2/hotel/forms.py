from django.contrib.auth.forms import UserCreationForm
from django import forms
# from .models import Guest
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["last_name", "first_name", "username", "password1"]