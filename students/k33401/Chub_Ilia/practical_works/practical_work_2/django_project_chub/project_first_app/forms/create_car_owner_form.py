from . import *
from ..models import CarOwner


class CreateCarOwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = ['id', 'first_name', 'last_name', 'birth_day', 'passport_number', 'address', 'nationality']
