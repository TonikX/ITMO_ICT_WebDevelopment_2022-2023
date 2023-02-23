from django import forms
from .models import *
  
  
class CarOwnerForm(forms.ModelForm):
  
    class Meta:
        model = CarOwner
  
        fields = [
            "last_name",
            "first_name",
            "birth_date",
            "passport",
            "home_address",
            "nationality",
        ]