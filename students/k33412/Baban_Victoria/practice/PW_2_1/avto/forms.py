from django import forms
from .models import Car_owner


# creating a form
class FormAddOwner(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Car_owner

        # specify fields to be used
        fields = [
            "last_name",
            "first_name",
            "date_of_birthday"
        ]
