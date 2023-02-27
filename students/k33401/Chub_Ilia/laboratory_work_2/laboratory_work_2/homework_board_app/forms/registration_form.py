from django.contrib.auth.forms import UserCreationForm
from ..models import BaseUserModel


class RegistrationForm(UserCreationForm):
    class Meta:
        model = BaseUserModel
        fields = ("username", "first_name", "last_name")
