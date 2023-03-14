from django.forms import ModelForm, TextInput, DateInput
from .models import Owner


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ['username', 'password', 'first_name', 'last_name', 'birthdate', 'passport_num', 'addres', 'nationality']
        widgets = {
            'username': DateInput(attrs={
                'placeholder': "Owner username",
            }),
            'password': DateInput(attrs={
                'placeholder': "Owner password",
            }),
            'first_name': TextInput(attrs={
                'placeholder': "Owner first name",
            }),
            'last_name': TextInput(attrs={
                'placeholder': "Owner last name",
            }),
            'birthdate': DateInput(attrs={
                'placeholder': "Owner birthdate",
            }),
            'passport_num': DateInput(attrs={
                'placeholder': "Owner passport num",
            }),
            'addres': DateInput(attrs={
                'placeholder': "Owner address",
            }),
            'nationality': DateInput(attrs={
                'placeholder': "Owner nationality",
            }),
        }
