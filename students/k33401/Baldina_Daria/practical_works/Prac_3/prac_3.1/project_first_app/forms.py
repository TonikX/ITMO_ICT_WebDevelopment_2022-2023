from django import forms
from .models import Car_owner

class CreateOwner(forms.ModelForm):
    class Meta:
        model = Car_owner
        fields = ['id_owner', 'last_name', 'first_name', 'birth_day']
