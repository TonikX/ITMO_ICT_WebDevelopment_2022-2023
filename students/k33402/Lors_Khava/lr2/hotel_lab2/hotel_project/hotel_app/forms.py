from django import forms
from .models import Client, Booking, Comment

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "first_name", "last_name",
            "birthday", "passport"
        ]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "client", "hotel", "room",
            "check_in_date", "check_out_date"
            
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "author", "hotel",
            "rating", "review_comment"
            
        ]