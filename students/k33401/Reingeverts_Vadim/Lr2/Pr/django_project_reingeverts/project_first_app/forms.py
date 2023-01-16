from django import forms

from .models import Car, CarOwner, Ownership, DriverLicense


class CarOwnerForm(forms.ModelForm):

    class Meta:
        model = CarOwner

        # specify fields to be used
        fields = [
            "last_name",
            "first_name",
            "username",
            "password",
            "ownership_id",
            "date_of_birth",
            "passport",
            "address",
            "nationality",
        ]
