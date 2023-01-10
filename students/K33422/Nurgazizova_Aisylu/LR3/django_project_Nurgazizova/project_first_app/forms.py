from django import forms
from .models import OwnerUser

class OwnerForm(forms.ModelForm):

    class Meta:
        # specify model to be used
        model = OwnerUser

        # specify fields to be used
        fields = [
            "username",
            "first_name",
            "last_name",
            "birthday",
            "passport",
            "address",
            "nationality"
        ]