from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm
from django.forms import PasswordInput

from .models import Driver, Vehicle


class DriverForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=PasswordInput)
    surname = forms.CharField(max_length=30, label='surname')
    name = forms.CharField(max_length=30, label='name')
    birth_date = forms.DateTimeField(label='birth date')
    passport = forms.CharField(max_length=11, label='passport')
    nationality = forms.CharField(max_length=30, label='nationality')
    address = forms.CharField(max_length=200, label='address')

    class Meta:
        model = Driver
        fields = [
            "username",
            "password",
            "surname",
            "name",
            "birth_date",
            "passport",
            "nationality",
            "address"
        ]
