from django import forms
from django.contrib.auth.models import User
from .models import *

class User_form(forms.ModelForm):
    username = forms.CharField(label="username")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")
    email = forms.CharField(label="Email address")
    first_name = forms.CharField(label="first_name")
    last_name = forms.CharField(label="last_name")

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

