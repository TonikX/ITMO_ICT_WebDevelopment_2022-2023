from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Passenger

class NewUserForm(UserCreationForm):
	class Meta:
		model = Passenger
		fields = ('username', 'last_name', 'first_name', 'middle_name', 'date_of_birth', 'passport_number')

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user