from django import forms
from .models import CarOwner


class CreateOwner(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = ['id_owner', 'last_name', 'first_name', 'birth_day', 'passport', 'address', 'nationality']
