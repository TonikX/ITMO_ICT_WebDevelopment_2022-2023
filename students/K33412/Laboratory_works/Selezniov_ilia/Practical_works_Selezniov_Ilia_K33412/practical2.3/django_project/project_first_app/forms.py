from django import forms
from .models import Car, Owner


class AddCarForm(forms.ModelForm):

    class Meta:
        model = Car

        fields = [
            "brand",
            "model",
            "color",
            "plate_number"
        ]
