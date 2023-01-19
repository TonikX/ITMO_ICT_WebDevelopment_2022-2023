from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
