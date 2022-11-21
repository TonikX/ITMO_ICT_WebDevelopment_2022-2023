from django import forms
from .models import Owner_Model


class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = Owner_Model
        fields = [
            'surname',
            'name',
            'birthday'
        ]
