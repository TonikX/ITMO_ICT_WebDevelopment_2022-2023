from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users_app.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)


class MyAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
