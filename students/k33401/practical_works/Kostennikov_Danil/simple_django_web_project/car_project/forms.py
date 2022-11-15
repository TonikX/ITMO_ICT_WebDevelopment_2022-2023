from django import forms
from .models import CarOwner


class CarOwnerCreateForm(forms.ModelForm):
    class Meta:
        model = CarOwner

        fields = [
            "last_name",
            "first_name",
            "birthdate"
        ]