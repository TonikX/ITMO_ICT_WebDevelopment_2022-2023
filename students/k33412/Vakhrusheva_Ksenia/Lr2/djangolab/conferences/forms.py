from django import forms

from .models import *


class RegisterForm(forms.ModelForm):
	class Meta:
		model = Author
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


class ConferenceRegisterForm(forms.ModelForm):
	class Meta:
		model = Performance
		fields = [
			'title',
			'description',
		]
		labels = {
			'title': 'Тема',
			'description': 'Описание'
		}


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = [
			'body',
			'rating'
		]
		widgets = {
			'body': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
		}
		labels = {
			'body': 'Текст комментария',
			'rating': 'Оценка'
		}
