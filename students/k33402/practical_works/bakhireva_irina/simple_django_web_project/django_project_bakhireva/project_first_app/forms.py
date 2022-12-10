from django import forms
from .models import *
  
  
class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'birthday',
            'passport',
            'address',
            'nationality',
        ]