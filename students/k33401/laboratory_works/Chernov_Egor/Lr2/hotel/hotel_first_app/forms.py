from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  # 'first_name',
                  # 'last_name',
                  'email',
                  )


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Login')
    password = forms.CharField(label='Password')
