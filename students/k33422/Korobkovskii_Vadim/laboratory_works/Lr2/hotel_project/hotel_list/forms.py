from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['guest', 'room', 'check_in', 'check_out']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'surname', 'name', 'phone_number', 'passport', 'email', 'birthday_date']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reservation', 'review', 'rating']
