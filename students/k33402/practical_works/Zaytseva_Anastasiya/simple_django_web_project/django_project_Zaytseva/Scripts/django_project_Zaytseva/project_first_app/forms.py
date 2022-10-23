from django import forms
from .models import CarOwner


class CarOwnerCreateForm(forms.ModelForm):
    class Meta:
        model = CarOwner

        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "date_of_birth",
            "passport_number",
            "address",
            "nationality",
        ]
