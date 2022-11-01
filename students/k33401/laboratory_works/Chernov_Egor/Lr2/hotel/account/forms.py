from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    # username = forms.CharField(label='Username')

    class Meta:
        model = User
        fields = ('username',
                  'email',)


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Login')
    password = forms.CharField(label='Password')
