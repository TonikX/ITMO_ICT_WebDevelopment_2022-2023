from .models import *
from django import forms


# form - create reservation
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        flight = forms.ModelChoiceField(queryset=Flight.objects)
        passenger = forms.ModelChoiceField(queryset=User.objects)
        seat = forms.CharField(max_length=15)
        ticket = forms.CharField(max_length=15, required=False)
        fields = ['passenger', 'flight', 'seat', 'ticket']


# form - create review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        author = forms.ModelChoiceField(queryset=User.objects)
        flight = forms.ModelChoiceField(queryset=Flight.objects)
        fields = ['author', 'flight', 'rating', 'comment']
