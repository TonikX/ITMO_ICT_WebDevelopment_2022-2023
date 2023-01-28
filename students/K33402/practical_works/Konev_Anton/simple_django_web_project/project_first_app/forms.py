from django import forms
from .models import CarOwner


class CreateOwner(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = ['owner_id', 'last_name', 'first_name', 'birth_date', 'passport', 'address', 'nationality', 'username']
