from django import forms
from practical.models import Owner


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            "username","first_name","last_name","date_of_birth",
            "passport","address","nationality"
        ]