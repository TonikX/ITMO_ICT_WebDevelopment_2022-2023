from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import AuthenticationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = ['luggage']


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['id_flight', 'text', 'rating']