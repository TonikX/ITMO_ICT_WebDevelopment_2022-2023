from django import forms
from project_first_app.models import Owner


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            "username","first_name","last_name","date_of_birth",
            "passport","address","nationality"
        ]