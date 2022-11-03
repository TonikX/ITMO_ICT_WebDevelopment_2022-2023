from django import forms
from .models import CarOwner


class CreateOwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner

        fields = [
            "first_name",
            "second_name",
            "date_of_birth"
        ]
