from django import forms
from .models import Motorist


class ExampleForm(forms.ModelForm):

    class Meta:
        model = Motorist

        fields = [
            "last_name",
            "first_name",
            "birth",
        ]
