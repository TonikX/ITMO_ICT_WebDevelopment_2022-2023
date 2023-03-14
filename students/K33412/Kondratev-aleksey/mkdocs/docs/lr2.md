# Лабораторная работа №2 Реализация простого сайта на django.

Реализовать веб сервис, в соответствии с вариантом из задания

* `account_created.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notification</title>
    <style>
        body {
            padding: 20px;
            padding-left: 50px;
        }
    </style>
</head>
<body>
    <p>The account created successfully!</p>
    <p>Please enter your personal information to start working.</p>
    <nav>
        <a href={{edit_link}}><strong>Go!</strong></a> |
        <a href="/profile/">Later</a>
    </nav>
</body>
</html>
```

* `all_tasks.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tasks</title>
    <style>
        body {
            padding-left: 50px;
        }

        ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
        }
    </style>
</head>
<header>
    <nav class="menu">
        <br>
        <a href="/profile/">Home</a> |
        <a href="/profile/all_tasks/">Tasks</a> |
        <a href="/profile/class_marks/subject_select">Class marks</a> |
        <a href="/accounts/{{user.id}}/update/">Edit profile</a> |
        <a href="/accounts/logout/">Log out</a><br>
        <br>
    </nav>
</header>
<body>
    <div class="main">
        <br>
        <ul>
            {% for task in task_list %}

            <li>Deadline: {{task.deadline}}</li>
            <li>Subject: {{task.subject}}</li>
            <li>Task: {{task.task_text}}</li>

            {% if task.id in hw_ids %}
                {% for answer in answers %}
                    {% if answer.homework_id == task.id %}
                        <p>Mark: {{ answer.mark }}</p>
                    {% endif %}
                {% endfor %}
            {% else %}
                <p><a href="/profile/all_tasks/answer?task_id={{task.id}}">Solve the task</a><br></p>
            {% endif %}

            <hr/>

            {% empty %}
            <p>No tasks yet.</p>

            {% endfor %}
        </ul>
    </div>
</body>
</html>
```

* `class_marks.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class marks</title>
    <style>
        body {
            padding-left: 50px;
        }

        table {
            border-top: 4px solid #000;
            border-collapse: collapse;
            text-align: center;
        }

        caption {
            text-align: left;
            padding: 10px;
        }

        thead {
            border-bottom: 4px solid #000;
        }

        tbody td  {
            text-align: left;
            padding-left: 5;
        }

        tbody td:last-child  {
            text-align: center;
        }

        td, th {
            border: 1px solid #000;
            padding: 10px;
            vertical-align: middle;
            line-height: 1.2;
        }
    </style>
</head>
<header>
    <nav class="menu">
        <br>
        <a href="/profile/">Home</a> |
        <a href="/profile/all_tasks/">Tasks</a> |
        <a href="/profile/class_marks/subject_select">Class marks</a> |
        <a href="/accounts/{{user.id}}/update/">Edit profile</a> |
        <a href="/accounts/logout/">Log out</a><br>
        <br>
    </nav>
</header>
<body>
    <table>
        <caption>
            Class: {{ user.group }}<br>
            Subject: {{ subject }}
        </caption>
        <thead>
            <tr>
                <th>Student</th>
                <th>Marks</th>
                <th>Average</th>
            </tr>
        </thead>
        <tbody>
            {% for student in class_students %}
            <tr>
                <td>{{student.surname}} {{student.name}} {{student.patronymic}}</td>
                {% for mark in marks %}
                    {% if forloop.counter == forloop.parentloop.counter %}
                        <td>{{ mark }}</td>
                    {% endif %}
                {% endfor %}
                {% for grade in average %}
                    {% if forloop.counter == forloop.parentloop.counter %}
                        <td>{{ grade }}</td>
                    {% endif %}
                {% endfor %}
            </tr>
            {% endfor %}
        </tbody>
    </table>

    <br>
    <a href="/profile/class_marks/subject_select">Select another subject</a>
</body>
</html>
```

* `profile_page.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
    <style>
        body {
            padding-left: 50px;
        }
    </style>
</head>
<header>
    <nav class="menu">
        <br>
        <a href="/profile/">Home</a> |
        <a href="/profile/all_tasks/">Tasks</a> |
        <a href="/profile/class_marks/subject_select">Class marks</a> |
        <a href={{edit_link}}>Edit profile</a> |
        <a href="/accounts/logout/">Log out</a><br>
        <br>
    </nav>
</header>
<body>
    {% if user.name == '' %}
        <p>Hello, {{ user.username }}!</p>
    {% else %}
        <p>Hello, {{ user.name }}!</p>
    {% endif %}
</body>
</html>
```

* `solution.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Answer</title>
    <style>
        body {
            padding-left: 50px;
        }
    </style>
</head>
<header>
    <nav class="menu">
        <br>
        <a href="/profile/">Home</a> |
        <a href="/profile/all_tasks/">Tasks</a> |
        <a href="/profile/class_marks/subject_select">Class marks</a> |
        <a href="/accounts/{{user.id}}/update/">Edit profile</a> |
        <a href="/accounts/logout/">Log out</a><br>
        <br>
    </nav>
</header>
<body>
    <p>Task: {{ task.task_text }}</p>
    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Send solution">
    </form>
</body>
</html>
```

* `start_page.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Start page</title>
    <style>
        body {
            padding: 20px;
            padding-left: 50px;
        }
    </style>
</head>
<body>
    <p>Welcome to the Homework Board!</p>
    <p>Please login or sign up to get started.</p>
    <nav>
        <a href="/accounts/login/">Log in</a> |
        <a href="/admin/login/">Log in as a teacher</a> |
        <a href="/accounts/signup/">Sign up</a>
    </nav>
</body>
</html>
```

* `subject_select.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subject select</title>
    <style>
        body {
            padding-left: 50px;
        }
    </style>
</head>
<header>
    <nav class="menu">
        <br>
        <a href="/profile/">Home</a> |
        <a href="/profile/all_tasks/">Tasks</a> |
        <a href="/profile/class_marks/subject_select">Class marks</a> |
        <a href="/accounts/{{user.id}}/update/">Edit profile</a> |
        <a href="/accounts/logout/">Log out</a><br>
        <br>
    </nav>
</header>
<body>
    <p>Click on the subject below to view class marks for it:</p>

    {% for subject in subjects %}
        <a href="/profile/class_marks?subject={{subject}}">{{ subject }}</a><br>
        <br>
    {% endfor %}
</body>
</html>
```

* `user_update.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User update</title>
    <style>
        body {
            padding-left: 50px;
        }
    </style>
</head>
<header>
    <nav class="menu">
        <br>
        <a href="/profile/">Home</a> |
        <a href="/profile/all_tasks/">Tasks</a> |
        <a href="/profile/class_marks/subject_select">Class marks</a> |
        <a href={{edit_link}}>Edit profile</a> |
        <a href="/accounts/logout/">Log out</a><br>
        <br>
    </nav>
</header>
<body>
    <p>Enter your personal information.</p>
    <p>User: {{object.username}}</p>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Save">
    </form>
</body>
</html>
```

* `settings.py`

```python
"""
Django settings for homework_board project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7%ii_szc&3vfg5($#nij*29(p#%!h!e0stc*7clee%!ja)(1)c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'board_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'homework_board.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'homework_board.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field typex
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'board_app.User'

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = '/profile/'
LOGIN_URL = '/accounts/login/'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_SIGNUP_REDIRECT_URL = '/accounts/created/'
```

* `urls.py`

```python
"""homework_board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('board_app.urls')),
]
```

* `admin.py`

```python
from django.contrib import admin
from .models import Homework, TaskCompletion, User

admin.site.register(Homework)
admin.site.register(TaskCompletion)
admin.site.register(User)
```

* `apps.py`

```python
from django.apps import AppConfig


class BoardAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board_app'

```

* `forms.py`

```python
from django import forms
from .models import TaskCompletion


class SolutionForm(forms.ModelForm):
    class Meta:
        model = TaskCompletion
        fields = ['answer']
        widgets = {
            'answer': forms.Textarea(attrs={'maxlength': 500, 'cols': 44, 'required': 'true'}),
        }

    def __init__(self, task, user, subject, task_text, *args, **kwargs):
        super(SolutionForm, self).__init__(*args, **kwargs)
        self.homework = task
        self.student = user
        self.subject = subject
        self.task_text = task_text

    def save(self, commit=True):
        instance = super(SolutionForm, self).save(commit=False)
        if not instance.homework_id:
            instance.homework = self.homework
            instance.student = self.student
            instance.subject = self.subject
            instance.task_text = self.task_text
        if commit:
            instance.save()
        return instance
```

* `models.py`

```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


CLASSES_LIST = (
    ('1-A', '1-A'),
    ('1-B', '1-B'),
    ('2-A', '2-A'),
    ('2-B', '2-B'),
    ('3-A', '3-A'),
    ('3-B', '3-B'),
)

class User(AbstractUser):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank=True)
    birthday = models.DateField(blank=True, null=True)
    group = models.CharField(max_length=4, choices=CLASSES_LIST)

class Homework(models.Model):
    subject = models.CharField(max_length=20)
    group = models.CharField(max_length=4, choices=CLASSES_LIST, blank=True)
    teacher = models.CharField(max_length=50)
    start_date = models.DateField()
    deadline = models.DateField()
    task_text = models.CharField(max_length=100)
    penalty_info = models.CharField(max_length=100)
    student = models.ManyToManyField(settings.AUTH_USER_MODEL, through='TaskCompletion')

class TaskCompletion(models.Model):
    MARKS_LIST = (
    ('-', '-'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    )
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    subject = models.CharField(max_length=20, blank=True)
    task_text = models.CharField(max_length=100, blank=True)
    answer = models.CharField(max_length=100)
    mark = models.CharField(max_length=1, choices=MARKS_LIST, blank=False, default='-')
```

* `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.StartPageView.as_view()),
    path('accounts/created/', views.NotificationView.as_view()),
    path('accounts/<int:pk>/update/', views.StudentUpdate.as_view()),
    path('profile/', views.ProfilePageView.as_view()),
    path('profile/all_tasks/', views.AllTasks.as_view()),
    path('profile/all_tasks/answer', views.solution_create),
    path('profile/class_marks/subject_select', views.subject_select),
    path('profile/class_marks', views.class_marks),
]
```

* `views.py`

```python
from django.shortcuts import render
from .models import User, Homework, TaskCompletion, CLASSES_LIST
from django.views.generic import TemplateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SolutionForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


class StartPageView(TemplateView):
    def get(self, request):
        return render(request, 'board_app/start_page.html')


class NotificationView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'

    def get(self, request):
        context = {}
        context["edit_link"] = f"/accounts/{self.request.user.id}/update/"
        return render(request, 'board_app/account_created.html', context)


class StudentUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'

    model = User
    template_name = 'board_app/user_update.html'
    fields = ["surname", "name", "patronymic", "birthday", "group"]
    success_url = '/profile/'


class ProfilePageView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'

    def get(self, request):
        context = {}
        context["edit_link"] = f"/accounts/{self.request.user.id}/update/"
        context["user"] = self.request.user
        return render(request, 'board_app/profile_page.html', context)


class AllTasks(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'

    def get(self, request):
        user = self.request.user
        if (user.group, user.group) not in CLASSES_LIST:
            return redirect(f"/accounts/{request.user.id}/update/")

        context = {}
        context['user'] = user
        context['task_list'] = Homework.objects.filter(group=user.group)

        answers = TaskCompletion.objects.filter(student_id=user.id)
        context['answers'] = answers

        context['hw_ids'] = []
        for answer in answers:
            context['hw_ids'].append(answer.homework_id)

        return render(request, 'board_app/all_tasks.html', context)


@login_required
def solution_create(request):
    task_id = request.GET.get('task_id')
    task = Homework.objects.get(pk=task_id)
    context = {}
    context["user"] = request.user

    if request.method == 'POST':
        form = SolutionForm(task, request.user, task.subject, task.task_text, request.POST)

        if form.is_valid():
            form.save()
            return redirect('/profile/all_tasks/')

    else:
        form = SolutionForm(task, request.user, task.subject, task.task_text)
        context["form"] = form
        context["task"] = Homework.objects.get(pk=task_id)

    return render(request, 'board_app/solution.html', context)


@login_required
def subject_select(request):
    user = request.user
    if (user.group, user.group) not in CLASSES_LIST:
        return redirect(f"/accounts/{request.user.id}/update/")

    context = {}
    context['user'] = user
    hw_list = Homework.objects.filter(group=user.group)

    context['subjects'] = []
    for hw in hw_list:
        if hw.subject not in context['subjects']:
            context['subjects'].append(hw.subject)

    return render(request, 'board_app/subject_select.html', context)


@login_required
def class_marks(request):
    context = {}
    user = request.user
    context['user'] = user

    class_students = User.objects.filter(group=user.group)
    class_students = class_students.order_by('surname', 'name', 'patronymic')
    context['class_students'] = class_students

    subject = request.GET.get('subject')
    context['subject'] = subject

    context['marks'] = []
    context['average'] = []
    for student in class_students:
        tasks_done = TaskCompletion.objects.filter(student_id=student.id, subject=subject)
        marks = ''
        marks_sum = 0
        n = 0
        for index, task in enumerate(tasks_done):
            marks += task.mark
            if index != len(tasks_done) - 1:
                marks += ', '
            if task.mark in '2345':
                marks_sum += int(task.mark)
                n += 1
        context['marks'].append(marks)
        if n != 0:
            context['average'].append(round((marks_sum / n), 2))
        else:
            context['average'].append('')

    return render(request, 'board_app/class_marks.html', context)
```