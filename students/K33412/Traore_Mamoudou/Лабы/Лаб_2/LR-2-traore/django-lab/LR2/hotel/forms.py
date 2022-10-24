from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Client, Booking, Review
from datetime import date


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Client
        fields = ('username', 'email', 'first_name', 'last_name', 'birthday', 'phone_number', 'password1', 'password2')


class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('client', 'room', 'people', 'start_date', 'end_date')
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'},
                                          format='d-%m-%Y'),
            'end_date': forms.DateInput(attrs={'type': 'date'},
                                        format='d-%m-%Y'),
        }

    def __init__(self, *args, **kwargs):
        super(CreateBookingForm, self).__init__(*args, **kwargs)
        self.fields['client'].disabled = True
        self.fields['room'].disabled = True

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        today = date.today()

        if start_date > end_date:
            raise forms.ValidationError("Your meeting shoud be earlier than last day!")

        if end_date < today:
            raise forms.ValidationError("Your date is in the past")


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('user', 'hotel', 'room', 'rating', 'date_start', 'date_end', 'text')
        widgets = {
            'date_start': forms.DateInput(attrs={'type': 'date'},
                                          format='d-%m-%Y'),
            'date_end': forms.DateInput(attrs={'type': 'date'},
                                        format='d-%m-%Y'),
            'text': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super(CreateReviewForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['room'].disabled = True
        self.fields['hotel'].disabled = True