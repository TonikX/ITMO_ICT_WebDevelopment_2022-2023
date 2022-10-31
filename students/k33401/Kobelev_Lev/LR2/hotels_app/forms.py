from django.forms import ModelForm
from .models import Review, Booking


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['date_start', 'date_end']
