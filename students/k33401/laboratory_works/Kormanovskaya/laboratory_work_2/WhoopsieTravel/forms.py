import datetime

from .models import Customer, TourConducting
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateCustomerForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password1', 'password2']


class BookingForm(forms.ModelForm):
    date_start = forms.DateField(label='Date start', initial=datetime.date.today())
    tourists = forms.IntegerField(label='Number of tourists', initial=1)
    contact_info = forms.CharField(max_length=200, label='Contact info')

    class Meta:
        model = TourConducting
        fields = [
            "date_start",
            "tourists",
            "contact_info",
            "tour",
            "customer"
        ]
