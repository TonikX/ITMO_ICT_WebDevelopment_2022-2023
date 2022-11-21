from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from hotel_first_app.models import Registration


class UpdateReserveForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('id_reg', 'id_employee', 'id_guest', 'id_room', 'status_reg',
                  'status_pay', 'check_in', 'check_out', 'booking')


class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  'email',)


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
