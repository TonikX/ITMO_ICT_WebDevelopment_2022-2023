from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


# form - create reservation
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room_type', 'num_of_guests', 'check_in_date', 'check_out_date', 'hotel']
        exclude = ['guest']


# form - create user
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


# form - create review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        reservation = forms.ModelChoiceField(queryset=Reservation.objects)
        fields = ['rating', 'comment']
        exclude = ['hotel', 'author']