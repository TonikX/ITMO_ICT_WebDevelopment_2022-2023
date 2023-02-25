from django import forms
from .models import *


class RegisterForm(forms.ModelForm):
	class Meta:
		model = Participant
		help_texts = {
			'username': None,
		}
		fields = [
			'username',
			'last_name',
			'first_name',
			'password',
		]
		labels = {
			'username': 'Логин',
			'last_name': 'Фамилия',
			'first_name': 'Имя',
			'password': 'Пароль'
		}
