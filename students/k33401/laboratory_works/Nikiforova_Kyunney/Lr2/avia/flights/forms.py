from django import forms

from .models import Passenger, Ticket, Comment


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = [
            "username", "password", "last_name",
            "first_name", "birth_date", "passport"
        ]


class CreateBooking(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["flight_number", "passport", "seat"]


class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["flight_number", "rating", "comment", "passenger"]
