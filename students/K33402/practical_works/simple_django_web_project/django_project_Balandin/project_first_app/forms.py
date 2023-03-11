from django import forms
from django.forms import PasswordInput

from .models import Owner


class OwnerForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=PasswordInput)
    surname = forms.CharField(max_length=30, label='surname')
    name = forms.CharField(max_length=30, label='name')
    birth_date = forms.DateTimeField(label='birth date')
    passport = forms.CharField(max_length=11, label='passport')
    nationality = forms.CharField(max_length=30, label='nationality')
    address = forms.CharField(max_length=200, label='address')

    class Meta:
        model = Owner
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
