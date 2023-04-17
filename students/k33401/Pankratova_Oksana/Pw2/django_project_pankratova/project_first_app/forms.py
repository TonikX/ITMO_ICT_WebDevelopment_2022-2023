from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.conf import settings


class ExampleForm(UserCreationForm):

    class Meta:
        model = CustomUser

        fields = ("last_name", "first_name", 'birth_date', "passport", "home_add", "nationality")
