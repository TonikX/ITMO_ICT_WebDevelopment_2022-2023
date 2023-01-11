from django import forms
from .models import Owner


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            "username", "password", "last_name", "first_name",
            "birth_date", "passport", "address", "nationality"
        ]