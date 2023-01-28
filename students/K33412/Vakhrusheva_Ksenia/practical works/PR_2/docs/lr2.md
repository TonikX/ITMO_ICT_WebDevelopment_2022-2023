# Лабораторная работа 2

* `conferences\admin.py`
```python
from django.contrib import admin

from .models import *


@admin.register(Conference, Author, Performance)
class Admin(admin.ModelAdmin):
	pass

```

* `conferences\apps.py`
```python
from django.apps import AppConfig


class ConferencesConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'conferences'

```

* `conferences\forms.py`
```python
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

```

* `conferences\models.py`
```python
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Conference(models.Model):
	name = models.CharField(max_length=50)
	subject = models.CharField(max_length=30)
	location = models.CharField(max_length=30)
	terms_of_participation = models.CharField(max_length=50)
	authors = models.ManyToManyField('Author', through='Performance')
	date = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self) -> str:
		return self.name


class Author(AbstractUser):
	last_name = models.CharField(max_length=30)
	first_name = models.CharField(max_length=30)

	def __str__(self) -> str:
		return f"{self.first_name} {self.last_name} ({self.username})"


class Performance(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	is_recommended = models.BooleanField(default=False)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	conference = models.ForeignKey(Conference, on_delete=models.CASCADE)

	def __str__(self) -> str:
		return f"{self.title} by {self.author.first_name} {self.author.last_name}"


class Comment(models.Model):
	post = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	rating = models.IntegerField(
		default=1,
		validators=[
			MaxValueValidator(10),
			MinValueValidator(1)
		]
	)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return 'Comment {} by {}'.format(self.body, self.name)

```

* `conferences\urls.py`
```python
from django.contrib.auth import views
from django.urls import path

from .views import *

urlpatterns = [
	path('login/', views.LoginView.as_view(), name='login'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	path('register/', register_view, name='register'),
	path('conferences/', conferences_view, name='conferences'),
	path('conferences/<int:pk>', conference_detail, name='conference_detail'),
	path('conferences/<int:pk>/register', conference_register, name='conference_register'),
	path('performances/', performance_view, name='performances'),
	path('performances/<int:pk>', performance_edit, name='performance_edit'),
	path('performances/<int:pk>/delete', performance_delete, name='performance_delete'),
	path('', index_view, name='index'),
]

```

* `conferences\views.py`
```python
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *


def index_view(request):
	conferences = Conference.objects.all()
	return render(request, 'index.html', {'conferences': conferences})


def register_view(request):
	context = {}

	form = RegisterForm(request.POST or None)

	if form.is_valid():
		u = form.save(commit=False)
		u.set_password(request.POST.dict()['password'])
		form.save()
		return redirect('/login/')
	context['form'] = form
	return render(request, 'registration/register.html', context)


def conferences_view(request):
	conferences = Conference.objects.all()
	return render(request, 'conferences/list_view.html', {'conferences': conferences})


def conference_detail(request, pk):
	try:
		conference = Conference.objects.get(pk=pk)
		performances = Performance.objects.filter(conference=conference)
		comments = Comment.objects.filter(post=pk)
		context = {
			'conference': conference,
			'performances': performances,
			'comments': comments
		}

		form = CommentForm(request.POST or None)
		context['form'] = form

		if form.is_valid():
			comment = form.save(commit=False)
			comment.author = Author.objects.get(pk=request.user.id)
			comment.post = conference
			comment.save()
	except Conference.DoesNotExist:
		raise Http404("Conference does not exist")
	return render(request, 'conferences/detail.html', context)


def conference_register(request, pk):
	context = {}
	if not request.user.is_authenticated:
		return redirect('/login/')
	form = ConferenceRegisterForm(request.POST or None)

	if form.is_valid():
		performance = form.save(commit=False)
		performance.author = Author.objects.get(pk=request.user.id)
		performance.conference = Conference.objects.get(pk=pk)
		performance.save()
		return redirect(f'/conferences/{pk}')
	context['form'] = form
	return render(request, 'conferences/register_performance.html', context)


def performance_view(request):
	if not request.user.is_authenticated:
		return redirect('/login/')

	conference = request.GET.get('conference', None)
	if conference:
		performances = Performance.objects.filter(author=request.user.id, conference=conference)
	else:
		performances = Performance.objects.filter(author=request.user.id)
	return render(request, 'performances/list_view.html', {'performances': performances})


def performance_edit(request, pk):
	context = {}
	if not request.user.is_authenticated:
		return redirect('/login/')

	instance = get_object_or_404(Performance, id=pk, author=request.user.id)
	form = ConferenceRegisterForm(request.POST or None, instance=instance)

	if form.is_valid():
		form.save()
		return redirect('/performances/')
	context['form'] = form
	context['pk'] = pk
	return render(request, 'performances/edit_performance.html', context)


def performance_delete(request, pk):
	if not request.user.is_authenticated:
		return redirect('/login/')

	instance = get_object_or_404(Performance, id=pk, author=request.user.id)
	print(instance)
	instance.delete()
	return redirect('/performances/')

```

* `conferences\templates\base.html`
```html
<!doctype  html>
<html lang="en">
<head>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"
	      crossorigin="anonymous">
	<title>Список конференций</title>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-light bg-light mx-3">
	<a class="navbar-brand" href="https://youtu.be/LqiHmZhO2to">Conferences site</a>
	<div class="collapse navbar-collapse justify-content-between " id="navbarNav">
		<ul class="navbar-nav mr-auto">
			<li class="nav-item active">
				<a class="nav-link" href="/">Главная</a>
			</li>
			<li class="nav-item">
				<a class="nav-link" href="/conferences/">Конференции</a>
			</li>
			<li class="nav-item">
				<a class="nav-link" href="/performances/">Мои выступления</a>
			</li>
		</ul>
		<span class="navbar-text">
        
      {% if user.is_authenticated %}
	      Привет, {{ user.username }}
	      <a class="nav-link d-inline-flex ms-2" href="/logout/">Выйти</a>
      {% else %}
	      <a class="nav-link" href="/login/">Login</a>
      {% endif %}</span>
	</div>
</nav>
<div class="container">
	<div class="row justify-content-center">
		<div class="text-center m-3">
			{% block main %}
			{% endblock %}
		</div>
	</div>
</div>
</body>
</html>
```

* `conferences\templates\index.html`
```html
{% extends 'base.html' %}
{% block main %}
	<h1>Конференции</h1>
	{% if conferences %}
		{% for conference in conferences %}
			<div class="card mb-3">
				<div class="card-body">
					<h4 class="card-title">{{ conference.name }}</h4>
					<h6 class="card-subtitle mb-2">{{ conference.subject }}</h6>
					<h6 class="card-subtitle mb-2 text-muted">{{ conference.location }} ({{ conference.date }})</h6>
					<p class="card-text">Список участников</p>
					<table class="table">

						<tbody>
						{% for participant in conference.authors.all %}
							<tr>
								<td>{{ participant.first_name }} {{ participant.last_name }}</td>
							</tr>
						{% endfor %}
						</tbody>
					</table>
					<a href="{% url 'conference_detail' conference.id %}" class="card-link">Подробнее</a>

				</div>
			</div>
		{% endfor %}
	{% else %}
		<div>Нет ни одной конференции</div>
	{% endif %}


{% endblock %}
```

* `conferences\templates\conferences\detail.html`
```html
{% extends 'base.html' %}
{% block main %}

	<h1>{{ conference.name }}</h1>
	<h3 class="text-muted">{{ conference.subject }}</h3>
	<h5>Место проведения: {{ conference.location }} ({{ conference.date|date:'d/m/Y H:i' }})</h3>
		<h5>Условия участия: {{ conference.terms_of_participation }}</h5>

		<table class="table my-5">
			<thead>
			<tr>
				<th scope="col">Докладчик</th>
				<th scope="col">Тема выступления</th>
				<th scope="col">Описание</th>
				<th scope="col">Рекомендован к публикации</th>
			</tr>
			</thead>
			<tbody>
			{% for performance in performances %}
				<tr>
					<td>{{ performance.author.first_name }} {{ performance.author.last_name }}</td>
					<td>{{ performance.title }}</td>
					<td>{{ performance.description }}</td>
					<td>{% if performance.is_recommended %} Да {% else %} Нет {% endif %}</td>
				</tr>
			{% endfor %}
			</tbody>
		</table>

		<h3 class="my-5">Комментарии</h3>

		{% for comment in comments %}
			<div class="card mb-3">
				<div class="card-body">
					<h4 class="card-title">{{ comment.author.first_name }} {{ comment.author.last_name }}</h4>
					<h6 class="card-subtitle mb-2 text-muted">{{ comment.created_on|date:'d/m/Y H:i' }}</h6>
					<p class="card-text">{{ comment.body }}</p>
					<h6 class="card-subtitle mb-2 text-muted">Оценка {{ comment.rating }}/10</h6>
				</div>
			</div>
		{% endfor %}

		{% if user.is_authenticated %}
			<h3 class="my-3">Оставьте комментарий</h3>
			<form method="post" class="my-3">
				{% csrf_token %}
				<input type="hidden" name="next" value="{{ next }}">

				{{ form.as_p }}

				<button type="submit" class="btn btn-primary btn-block">Оставить комментарий</button>
			</form>
			<a href="{% url 'conference_register' conference.id %}">Подать заявку</a><br>
			<a href="{% url 'performances' %}?conference={{ conference.id }}">Мои заявки на эту конференцию</a>
		{% endif %}
		<br>
		<a href="{% url 'conferences' %}">К списку конференций</a>



{% endblock %}
```

* `conferences\templates\conferences\list_view.html`
```html
{% extends 'base.html' %}
{% block main %}
	<h1>Конференции</h1>
	{% if conferences %}
		<div class="list-group">
			{% for conference in conferences %}
				<a href="{% url 'conference_detail' conference.id %}"
				   class="list-group-item list-group-item-action">{{ conference.name }}</a>
			{% endfor %}
		</div>
	{% else %}
		<div>Нет ни одной конференции</div>
	{% endif %}
{% endblock %}
```

* `conferences\templates\conferences\register_performance.html`
```html
{% extends  'base.html' %}


{% block main %}
	<div class="card">
		<div class="card-body">
			<h4 class="card-title">Подать заявку</h4>

			<form method="post">
				{% csrf_token %}
				<input type="hidden" name="next" value="{{ next }}">

				{{ form.as_p }}

				<button type="submit" class="btn btn-primary btn-block">Подтвердить</button>
			</form>
		</div>
	</div>
{% endblock %}
```

* `conferences\templates\performances\edit_performance.html`
```html
{% extends  'base.html' %}


{% block main %}
	<div class="card">
		<div class="card-body">
			<h4 class="card-title">Отредактировать заявку</h4>

			<form method="post">
				{% csrf_token %}
				<input type="hidden" name="next" value="{{ next }}">

				{{ form.as_p }}

				<button type="submit" class="btn btn-primary btn-block">Подтвердить</button>
				<a href="{% url 'performance_delete' pk %}" class="btn btn-danger btn-block">Удалить</a>

			</form>

		</div>
	</div>
{% endblock %}
```

* `conferences\templates\performances\list_view.html`
```html
{% extends 'base.html' %}
{% block main %}
	<div class="list-group">
		{% if performances %}
			{% for performance in performances %}
				<a href="{% url 'performance_edit' performance.id %}"
				   class="list-group-item list-group-item-action">{{ performance.title }}
					({{ performance.conference.name }})</a>
			{% endfor %}
		{% else %}
			<div>Вы не создали ни одного выступления</div>
		{% endif %}
	</div>

{% endblock %}
```

* `conferences\templates\registration\logged_out.html`
```html
{% extends 'base.html' %}
{% block main %}

	<p>Вы вышли!</p>
	<a href="{% url 'login' %}">Войти</a>

{% endblock %}
```

* `conferences\templates\registration\login.html`
```html
{% extends  'base.html' %}


{% block main %}
	<div class="card">
		<div class="card-body">
			<h4 class="card-title">Войдите в свой аккаунт</h4>

			<form method="post">
				{% csrf_token %}
				<input type="hidden" name="next" value="{{ next }}">

				{{ form.as_p }}

				<button type="submit" class="btn btn-primary btn-block">Войти</button>
			</form>
			<a href="{% url 'register' %}" class="card-link">Нет учетной записи?</a>
		</div>
	</div>
{% endblock %}
```

* `conferences\templates\registration\register.html`
```html
{% extends  'base.html' %}


{% block main %}
	<div class="card">
		<div class="card-body">
			<h4 class="card-title">Регистрация</h4>

			<form method="post">
				{% csrf_token %}
				<input type="hidden" name="next" value="{{ next }}">

				{{ form.as_p }}

				<button type="submit" class="btn btn-primary btn-block">Подтвердить</button>
			</form>
			<a href="{% url 'login' %}" class="card-link">Уже есть учетная запись?</a>
		</div>
	</div>
{% endblock %}
```

