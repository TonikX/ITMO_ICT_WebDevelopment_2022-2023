# Лабораторная работа №2 Мамедов Тогрул К33402

# Настройки


import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@!dm_pc2ut%+5x$)sp_co3d)=2zzdg&q5=x1=il2gk*s2$ihd3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'labs',
    'users',
    'work_space',
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

ROOT_URLCONF = 'labs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
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

WSGI_APPLICATION = 'labs.wsgi.application'


AUTH_USER_MODEL = 'users.User'


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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Модели

from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class SubjectChoices(models.TextChoices):
    MATH = 'математика'
    PHYSICS = 'физика'
    BIOLOGY = 'биология'


class CreateTask(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE,)
    subject = models.CharField(max_length=30, choices=SubjectChoices.choices)
    task = models.TextField(null=True)
    grade = models.IntegerField(null=True)
    sanctions = models.TextField(null=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    data_finish = models.DateTimeField(null=True)

    def __str__(self):
        return self.task


class AnswerTask(models.Model):
    task = models.ForeignKey(CreateTask, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE,)
    answer = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    assessment = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.answer


# Вью

from django.shortcuts import render, redirect

from work_space.forms import CreateTaskForm, AnswerTaskForm
from work_space.models import CreateTask, AnswerTask
from django.contrib.auth import get_user_model

User = get_user_model()


def staf_only(func):
    def check_user(request, *args, **kwargs):
        if request.user.is_staff:
            return func(request, *args, **kwargs)
        return redirect('auth:signup')

    return check_user


@staf_only
def TaskCreate(request):
    if request.method == 'POST':
        form = CreateTaskForm(
            request.POST
        )
        print(form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.teacher = request.user
            instance.save()
            return redirect('work:task_list')
    else:
        form = CreateTaskForm()
    context = {
        'form': form,
    }
    return render(request, 'work_space/task_create.html', context=context)


def TaskList(request):
    tasks = CreateTask.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'work_space/task_list.html', context=context)


def AnswerCreate(request, pk):
    task = CreateTask.objects.get(pk=pk)
    if request.method == 'POST':
        form = AnswerTaskForm(
            request.POST
        )
        if form.is_valid():
            instance = form.save(commit=False)
            instance.student = request.user
            instance.save()
            return redirect('work:task_list')
    else:
        form = AnswerTaskForm()
    context = {
        'form': form,
        'task': task,
    }
    return render(request, 'work_space/task_answer.html', context=context)


def AnswerList(request):
    answers = AnswerTask.objects.all()
    context = {
        'answers': answers,
    }
    return render(request, 'work_space/answer_list.html', context=context)


def AssessmentList(request):
    users = Users.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'work_space/assessment_list.html', context=context)

# Формы

from django import forms

from work_space.models import CreateTask, AnswerTask


class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = CreateTask
        fields = ['subject', 'task', 'sanctions', 'data_finish']



class AnswerTaskForm(forms.ModelForm):

    class Meta:
        model = AnswerTask
        fields = ['answer', 'task']


# Админ

from django.contrib import admin

from work_space.models import CreateTask, AnswerTask


class CreateTaskAdmin(admin.ModelAdmin):
    list_display = (
        'teacher',
        'subject',
        'task',
    )
    search_fields = ('subject',)
    list_filter = ('teacher',)
    empty_value_display = '-пусто-'


class AnswerTaskAdmin(admin.ModelAdmin):
    list_display = (
        'task',
        'student',
        'answer',
        'date',
        'assessment',
    )
    search_fields = ('student',)
    list_filter = ('date',)
    empty_value_display = '-пусто-'


admin.site.register(CreateTask, CreateTaskAdmin)
admin.site.register(AnswerTask, AnswerTaskAdmin)


