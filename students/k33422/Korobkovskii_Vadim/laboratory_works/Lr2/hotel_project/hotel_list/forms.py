from django.contrib import admin
from django.forms import ModelChoiceField

from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room', 'check_in', 'check_out']


class ReservationUpdateForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room', 'check_in', 'check_out']

    def __init__(self, *args, **kwargs):
        super(ReservationUpdateForm, self).__init__(*args, **kwargs)
        self.fields["room"].disabled = True


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'surname', 'name', 'phone_number', 'passport', 'email', 'birthday_date']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reservation', 'review', 'rating']

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields["reservation"].disabled = True


class ReviewUpdateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reservation', 'review', 'rating']

    def __init__(self, *args, **kwargs):
        super(ReviewUpdateForm, self).__init__(*args, **kwargs)
        self.fields["reservation"].disabled = True

