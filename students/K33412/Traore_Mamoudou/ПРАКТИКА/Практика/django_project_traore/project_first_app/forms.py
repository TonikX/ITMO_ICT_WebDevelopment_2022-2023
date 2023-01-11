from django import forms
from .models import OwnerUser

class OwnerForm(forms.ModelForm):

    class Meta:
        model = OwnerUser
        fields = ['username', 'password', 'first_name', 'last_name', 'birthday', 'passport', 'address', 'nationality']