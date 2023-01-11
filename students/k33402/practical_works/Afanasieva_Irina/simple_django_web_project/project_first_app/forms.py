from django import forms
from project_first_app.models import Owner, Car

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner

        fields = [
            "username",
            "password",
            "owner_name",
            "owner_surname",
            "owner_birth",
            "passport",
            "address",
            "nationality"
        ]