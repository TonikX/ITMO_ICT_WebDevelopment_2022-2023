from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

from Conferences.models import User, Сonference, Comment


class RegistrUser(forms.ModelForm):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=60)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name"]



class ConferenceApply(forms.ModelForm):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=60)

    class Meta:
        model = Сonference
        fields = ["email", "password"]

class CreateComment(forms.ModelForm):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=60)

    class Meta:
        model = Comment
        fields = ["email", "password", "comment", "rank"]
