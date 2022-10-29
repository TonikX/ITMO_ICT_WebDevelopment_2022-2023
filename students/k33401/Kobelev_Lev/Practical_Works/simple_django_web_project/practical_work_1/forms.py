from django import forms
from .models import Owner


class CreateOwner(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['username', 'password', 'first_name', 'second_name', 'birthday', 'passport', 'address', 'nationality']
