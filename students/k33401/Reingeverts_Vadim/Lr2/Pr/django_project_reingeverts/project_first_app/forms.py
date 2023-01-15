from django import forms

from .models import Car, CarOwner, Ownership, DriverLicense


class CarOwnerForm(forms.ModelForm):

    class Meta:
        model = CarOwner

        # specify fields to be used
        fields = [
            "ownership_id",
            "last_name",
            "first_name",
            "date_of_birth",
        ]
