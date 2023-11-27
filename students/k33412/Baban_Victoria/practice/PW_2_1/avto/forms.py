from django import forms
from .models import Car_owner


class FormAddOwner(forms.ModelForm):

    class Meta:

        model = Car_owner

        fields = [
            "last_name",
            "first_name",
            "date_of_birthday",
            'passport',
            'address',
            'nationality'
        ]
