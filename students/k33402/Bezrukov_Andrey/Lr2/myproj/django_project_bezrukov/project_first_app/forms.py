from django import forms
from project_first_app.models import CarOwnerUser


class CarOwnerCreateForm(forms.ModelForm):

    class Meta:
        model = CarOwnerUser
        fields = ["username", "password", "first_name", "last_name", "date_of_birth", "passport", "home_address", "nationality"]