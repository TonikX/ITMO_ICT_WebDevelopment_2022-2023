from django import forms
from django.contrib.auth.forms import UserCreationForm

from . import models


class UserSignUpForm(UserCreationForm):

    class Meta:
        model = models.User

        fields = [
            "first_name",
            "last_name",

            "username",
            "email",
        ]


class UserLogInForm(forms.ModelForm):

    class Meta:
        model = models.User

        fields = ["username", "password"]
