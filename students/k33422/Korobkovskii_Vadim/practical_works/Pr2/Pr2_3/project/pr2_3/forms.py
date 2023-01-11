import imp
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Owner, Car


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            "surname",
            "name",
            "birthday_date",
            "passport",
            "address",
            "nationality",
        ]


class OwnerCreateForm(UserCreationForm):
    class Meta:
        model = Owner
        fields = [
            "surname",
            "name",
            "birthday_date",
            "passport",
            "address",
            "nationality",
        ]


class OwnerUpdateForm(UserChangeForm):
    class Meta:
        model = Owner
        fields = [
            "surname",
            "name",
            "birthday_date",
            "passport",
            "address",
            "nationality",
        ]
