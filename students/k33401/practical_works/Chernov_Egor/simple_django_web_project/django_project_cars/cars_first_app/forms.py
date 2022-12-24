from django import forms
from .models import Driver


# creating a form
class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = [
            'username',
            'first_name',
            'last_name',
            'birthday',
            'passport',
            'address',
            'nationality',
            'password',
        ]
