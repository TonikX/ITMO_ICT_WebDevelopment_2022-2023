from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'passport', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'passport': forms.NumberInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    username.widget.attrs.update({'class': 'form-input'})
    password.widget.attrs.update({'class': 'form-input'})

    class Meta:
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-input'})
        }


class ReviewForm(forms.Form):
    RATE_CHOICES = [i for i in Comment.rate_choices]
    text = forms.CharField()
    rating = forms.MultipleChoiceField(choices=RATE_CHOICES)
    rating.widget.attrs.update({'class': 'form-input'})
    text.widget.attrs.update({'class': 'form-input'})
