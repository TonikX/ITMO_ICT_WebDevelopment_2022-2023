from django import forms
from .models import Owner


class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            'last_name',
            'first_name',
            'birth_date',
            'pass_number',
            'address',
            'nat'
        ]
