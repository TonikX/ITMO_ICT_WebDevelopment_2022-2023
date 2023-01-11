from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import User


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'lastname', 'first_name', 'date_of_birth', 'passport')


class FeedbackForm(forms.Form):
    comment = forms.CharField(label='Comment', max_length=100)
    rating = forms.IntegerField(label='Rating', validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
    ])
    date = forms.DateField(label='Flight date')


class TicketUpdateForm(forms.Form):
    seat = forms.CharField(label='Seat', max_length=3)


class BookForm(forms.Form):
    type = forms.ChoiceField(choices=(('TO', 'Arrival'),
                                      ('FROM', 'Departure')))
    seat = forms.CharField(label="Seat", max_length=3)
