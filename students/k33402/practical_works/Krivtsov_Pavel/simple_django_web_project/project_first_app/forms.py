from django import forms
from .models import CarOwner
from django.contrib.auth.forms import UserCreationForm


class CreateOwnerForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'from-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'from-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'from-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'from-input'}))
    second_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'from-input'}))
    date_of_birth = forms.DateTimeField(label='Дата рождения', widget=forms.DateInput(attrs={'type': 'date'}))
    passport_number = forms.CharField(label='Номер паспорта', widget=forms.TextInput(attrs={'class': 'from-input'}))
    nationality = forms.CharField(label='Национальность', widget=forms.TextInput(attrs={'class': 'from-input'}))
    address = forms.TextInput()

    class Meta:
        model = CarOwner

        fields = [
            "username",
            "password1",
            "password2",
            "first_name",
            "second_name",
            "date_of_birth",
            "passport_number",
            "nationality",
            "address"
        ]
