from django.forms import ModelForm
from .models import Registration, Car, Driver, Comment, Race
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegForm(ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['car_model', 'number', 'car_class', 'speed', 'weight', 'length', 'mileage']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateDriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'surname', 'team', 'country', 'driver_class', 'age', 'experience']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class RaceForm(ModelForm):
    class Meta:
        model = Race
        fields = '__all__'
