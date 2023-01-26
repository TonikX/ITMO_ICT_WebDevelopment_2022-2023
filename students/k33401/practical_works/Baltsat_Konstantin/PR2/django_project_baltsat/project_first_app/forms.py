from django import forms
from project_first_app.models import Car_owner


class CreateOwner(forms.ModelForm):
    class Meta:
        model = Car_owner
        fields = ['id_owner', 'last_name', 'first_name', 'birth_date', 'passport', 'address', 'nationality']
