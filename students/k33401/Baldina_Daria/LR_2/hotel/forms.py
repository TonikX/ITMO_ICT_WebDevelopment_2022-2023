from django import forms
from .models import Reservation, Comment

class CreateReservation(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room', 'guest', 'arrival_date', 'departure_date']

class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['reservation', 'text', 'rate', 'sing_author']