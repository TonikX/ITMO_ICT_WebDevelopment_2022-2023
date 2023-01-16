from django import forms

from .models import *


class OwnerForm(forms.ModelForm):
	class Meta:
		model = Owner
		fields = [
			'username',
			'password',
			'last_name',
			'first_name',
			'date_of_birth',
			'address',
			'nationality',
			'passport',
		]
