from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from Conferences.models import User, Сonference, Comment


class RegistrUser(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","first_name","last_name")


class MyAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User

#class ConferenceApply(forms.ModelForm):
   # email = forms.CharField(max_length=50)
    #password = forms.CharField(max_length=60)

 #   class Meta:
  #      model = Сonference
        #fields = ["email", "password"]

class CreateComment(forms.ModelForm):
    #email = forms.CharField(max_length=50)
    #password = forms.CharField(max_length=60)
    #"email", "password",
    class Meta:
        model = Comment
        fields = ["comment", "rank"]
