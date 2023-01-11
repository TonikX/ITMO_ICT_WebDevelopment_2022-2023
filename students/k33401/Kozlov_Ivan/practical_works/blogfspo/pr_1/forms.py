import imp

from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from pr_1.models import Transport_owner


class Transport_owner_form(forms.ModelForm):
    class Meta:
        model = Transport_owner
        fields = [
            "id_owner",
            "last_name",
            "first_name",
            "date_birthday",
            "passport_number",
            "home_adress",
            "national",
        ]


class Transport_owner_user_create(UserCreationForm):
    class Meta:
        model = Transport_owner
        fields = [
            "id_owner",
            "last_name",
            "first_name",
            "date_birthday",
            "passport_number",
            "home_adress",
            "national",
        ]


class Transport_owner_user_change(UserChangeForm):
    class Meta:
        model = Transport_owner
        fields = [
            "id_owner",
            "last_name",
            "first_name",
            "date_birthday",
            "passport_number",
            "home_adress",
            "national",
        ]
