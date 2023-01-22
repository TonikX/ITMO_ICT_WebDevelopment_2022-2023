#Лабораторная работа 3. Реализация серверной части на django rest. 
#Документирование API.

## Цель работы: овладеть практическими навыками реализации серверной части (backend) приложений средствами Django REST framework.

* `models.py`
```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE


class User(AbstractUser):
    tel = models.CharField(verbose_name='Телефон', max_length=15, null=True, blank=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'tel']

    def __str__(self):
        return self.username


class Instance(models.Model):
    id_instance = models.AutoField("ID_экземпляра", primary_key=True)
    section = models.CharField(max_length=20, verbose_name='Раздел')
    code = models.CharField(max_length=20, verbose_name='Артикул')
    year = models.IntegerField(verbose_name='Год издания')
    conditions = (
        ('х', 'хорошее'),
        ('у', 'удовлетворительное'),
        ('с', 'старое'),
    )
    condition = models.CharField(max_length=1, choices=conditions, verbose_name='Состояние экземпляра')
    book = models.ForeignKey('Book', verbose_name='Книга', on_delete=CASCADE)

    def __str__(self):
        return self.code


class Book(models.Model):
    id_book = models.AutoField("ID_книги", primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название')
    author = models.CharField(max_length=70, verbose_name="ФИО автора")
    publisher = models.CharField(max_length=30, verbose_name='Издательство')

    def __str__(self):
        return self.name


class Reader(models.Model):
    ticket = models.CharField(max_length=20, verbose_name='Номер читательского билета')
    name = models.CharField(max_length=70, verbose_name="ФИО")
    passport = models.CharField(max_length=20, verbose_name='Номер паспорта')
    birth_date = models.DateField(verbose_name='Дата рождения')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    educations = (
        ('н', 'начальное'),
        ('с', 'среднее'),
        ('в', 'высшее'),
    )
    education = models.CharField(max_length=1, choices=educations, verbose_name='Образование')
    degree = models.BooleanField(default=False, verbose_name='Наличие ученой степени')
    registration_date = models.DateField(verbose_name='Дата регистрации')
    instances = models.ManyToManyField('Instance', verbose_name='Взятые книги', through='ReaderBook',
                                       related_name='reader_book')
    room = models.ForeignKey('Room', verbose_name='Зал, за которым закреплен читатель', on_delete=CASCADE, null=True)

    def __str__(self):
        return self.name


class ReaderRoom(models.Model):
    reader = models.ForeignKey('Reader', verbose_name='Читатель', on_delete=CASCADE)
    room = models.ForeignKey('Room', verbose_name='Зал', on_delete=CASCADE)
    date = models.DateField(verbose_name='Дата закрепления зала', null=True)


class BookInst(models.Model):
    inst = models.ForeignKey('Instance', verbose_name='Экземпляр', on_delete=CASCADE)
    book = models.ForeignKey('Book', verbose_name='Книга', on_delete=CASCADE)


class ReaderBook(models.Model):
    reader = models.ForeignKey('Reader', verbose_name='Читатель', on_delete=CASCADE)
    book = models.ForeignKey('Instance', verbose_name='Экземпляр', on_delete=CASCADE)
    date = models.DateField(verbose_name='Дата выдачи экземпляра книги', null=True)


class BookRoom(models.Model):
    book = models.ForeignKey('Instance', verbose_name='Книга', on_delete=CASCADE)
    room = models.ForeignKey('Room', verbose_name='Зал', on_delete=CASCADE)


class Room(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    capacity = models.IntegerField(verbose_name='Вместимость')
    books = models.ManyToManyField('Instance', verbose_name='Книги', through='BookRoom', related_name='book_room')

    def __str__(self):
        return self.name
```

* `serializers.py`
```python
from django.utils import timezone
from rest_framework import serializers
from .models import *


class ReaderSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(read_only=True, many=True, slug_field='books')

    class Meta:
        model = Reader
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = "__all__"


class ReaderBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaderBook
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')

    class Meta:
        model = Room
        fields = "__all__"


class BookRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRoom
        fields = "__all__"


class ReaderRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaderRoom
        fields = "__all__"


class BookInstSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInst
        fields = "__all__"


class ReaderInstsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ["instances"]


class RecentlyBookDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaderBook
        fields = ["reader"]

```

* `urls.py`
```python
from django.urls import path
from .views import *

urlpatterns = [
    path('readers/list/', ReaderListAPIView.as_view()),
    path('readers/create/', CreateReader.as_view()),
    path('readers/<int:pk>/', OneReader.as_view()),
    path('books/list/', BookListAPIView.as_view()),
    path('books/create/', CreateBook.as_view()),
    path('books/<int:pk>/', OneBook.as_view()),
    path('inst/list/', InstanceListAPIView.as_view()),
    path('inst/create/', CreateInstance.as_view()),
    path('inst/<int:pk>/', OneInstance.as_view()),
    path('rooms/list/', RoomListAPIView.as_view()),
    path('rooms/create/', RoomCreateAPIView.as_view()),
    path('rooms/<int:pk>/', OneRoom.as_view()),
    path('book/readers/', BookReaders.as_view()),
    path('book/room/', RoomBook.as_view()),
    path('room/readers/', RoomReader.as_view()),
    path('book/inst/', BookInst.as_view()),
    path('readers/inst/<int:pk>', ReadersInst.as_view()),
    path('book/recently/', RecentlyBookDate.as_view()),
]
```

* `settings.py`

```python
"""
Django settings for library_project project.

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
SECRET_KEY = 'django-insecure-3&m=g&x2aqy-w#aoqwqlgsv_5s-22mq_e&r2_(7_v)&%9u#6c+'

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
    'library',
    'rest_framework',
    'djoser',
    'rest_framework.authtoken',
    'drf_yasg'
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

ROOT_URLCONF = 'library_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'library_project.wsgi.application'


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

AUTH_USER_MODEL = 'library.User'

ROOT_URLCONF = 'library_project.urls'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}
```

