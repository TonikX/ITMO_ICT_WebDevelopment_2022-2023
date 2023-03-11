import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class BuyTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "passenger_name",
            "passenger_surname",
            "passenger_passport",
        ]
