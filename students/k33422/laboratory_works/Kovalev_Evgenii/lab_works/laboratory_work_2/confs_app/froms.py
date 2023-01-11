from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'})),
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя'),
    surname = forms.CharField(label='Фамилия'),
    lastname = forms.CharField(label='Отчество'),
    password1 = forms.CharField(label='Пароль'),
    password2 = forms.CharField(label='Подтверждение пароля')

    class Meta:
        model = User
        fields = ('username', 'surname', 'lastname', 'password1', 'password2')