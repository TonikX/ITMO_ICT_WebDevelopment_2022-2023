from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
# from django.contrib.auth.models import Group


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  # 'first_name',
                  # 'last_name',
                  'email',
                  )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username',
                  # 'first_name',
                  # 'last_name',
                  'email',
                  )
