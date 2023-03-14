from django import forms
from django import forms
from .models import Owner

class CreateOwner(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['id_owner', 'last_name', 'first_name', 'birth_day']