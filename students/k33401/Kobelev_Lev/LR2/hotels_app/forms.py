from django.forms import ModelForm, ValidationError
from .models import Review, Booking


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['date_start', 'date_end']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("date_start")
        end_date = cleaned_data.get("date_end")
        if end_date < start_date:
            raise ValidationError("End date should be greater than start date.")
