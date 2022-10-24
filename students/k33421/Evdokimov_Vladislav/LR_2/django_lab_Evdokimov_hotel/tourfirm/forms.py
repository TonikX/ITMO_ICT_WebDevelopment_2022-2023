from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'passport_data', 'phone_number']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('username', 'start_date', 'tour', 'end_date', 'user_rating', 'comment', 'date_of_publication')

    def __init__(self, *args, **kwargs):
        super(CreateCommentForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True


class CreateReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('username', 'tour', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super(CreateReservationForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True
        self.fields['tour'].disabled = True
