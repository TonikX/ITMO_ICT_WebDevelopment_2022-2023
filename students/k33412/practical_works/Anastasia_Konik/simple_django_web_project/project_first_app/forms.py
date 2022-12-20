from django import forms
from .models import CarOwner


class CreateCarOwner(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = ['owner_id', 'last_name', 'first_name', 'birthday', 'passport', 'address', 'nationality']
