from django import forms
from project_first_app.models import CarOwnerUser

class CarOwnerCreateForm(forms.ModelForm):

    class Meta:
        model = CarOwnerUser
        fields = ["id_owner", "name", "surname", "date_of_birth"]