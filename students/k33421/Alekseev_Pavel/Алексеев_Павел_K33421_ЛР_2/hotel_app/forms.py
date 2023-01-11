from django import forms
from .models import Guest, Accommodation, Comment


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = [
            "username", "password", "last_name",
            "first_name", "birth_date", "passport"
        ]


class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = [
            "check_in_date", "check_out_date",
            "guest", "room"
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "comment", "rating",
            "guest", "hotel"
        ]
