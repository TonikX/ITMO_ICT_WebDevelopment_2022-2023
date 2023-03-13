from django.forms import ModelForm, TextInput, DateInput
from .models import Owner


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ['first_name', 'last_name', 'birthdate']
        widgets = {
            'first_name': TextInput(attrs={
                'placeholder': "Owner first name",
            }),
            'last_name': TextInput(attrs={
                'placeholder': "Owner last name",
            }),
            'birthdate': DateInput(attrs={
                'placeholder': "Owner birthdate",
            }),
        }
