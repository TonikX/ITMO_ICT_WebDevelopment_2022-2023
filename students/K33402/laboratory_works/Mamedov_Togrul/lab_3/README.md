# Лабораторная работа №3 Мамедов Тогрул К33402

# Описание

Проект labsdrf представляет из себя api для сайта библиотеки, где можно просмотреть список книг и числятся ли они 
в данный момент за читателем


# Стек технологий
Проект написан на Python с использованием Django REST Framework
база данных - SQLite3 


# Ресурсы проекта

<br>Ресурс book : создание, изменение и удаление книги либо закрепить ее за читателем и установить срок сдачи
<br>Ресурс storage: создание, изменение и удаление нового помещения библиотеки
<br>Ресурс library: создание, изменение и удаление новой библиотеки 
<br>Ресурс users: создание, изменение и удаление нового читательского билета(пользователя)


# Настройки

from pathlib import Path

from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#wg57*1kn*qez8dp5lhvtxh!a71ys+_124ogstb_$dc$17za#6'

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
    'rest_framework.authtoken',
    'djoser',
    'rest_framework',
    'library',
    'drf_yasg',
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

ROOT_URLCONF = 'drf.urls'

AUTH_USER_MODEL = 'library.User'

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

WSGI_APPLICATION = 'drf.wsgi.application'


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

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,
    'SERIALIZERS': {
        'user': 'library.serializers.UserSerializer',
        'user_create': 'library.serializers.UserSerializer',
    },
}


REST_FRAMEWORK = {
     'DEFAULT_PERMISSION_CLASSES': [
         'rest_framework.permissions.IsAuthenticated',
     ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        ],
}

SWAGGER_SETTINGS = {
   'SECURITY_DEFINITIONS': {
      'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
      }
   }
}

SIMPLE_JWT = {
   'ACCESS_TOKEN_LIFETIME': timedelta(days=10),
   'AUTH_HEADER_TYPES': ('Bearer',),
}


# Модели

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Базовый пользователь """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Reader(User):
    """ Читатель """
    age = models.IntegerField()

    class Meta:
        verbose_name = 'Reader'
        verbose_name_plural = 'Readers'


class Librarian(User):
    """ Библиотекарь """
    library = models.ForeignKey('Library', on_delete=models.CASCADE, related_name='librarians')

    class Meta:
        verbose_name = 'Librarian'
        verbose_name_plural = 'Librarians'


class Library(models.Model):
    """ Библиотека """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'


class ReaderTicket(models.Model):
    """ Читательский билет """
    registration_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()
    owner = models.OneToOneField('Reader', on_delete=models.CASCADE, related_name='read_ticket')
    library = models.ForeignKey('Library', on_delete=models.CASCADE)


class BookStorageLocation(models.Model):
    """ Местонахождение книги """
    room = models.CharField(max_length=100)
    shelf = models.IntegerField()
    library = models.ForeignKey('Library', on_delete=models.CASCADE, related_name='books')
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='storage_location')

    def __str__(self):
        return f'{self.book.name}: {self.room} - {self.shelf}'


class Book(models.Model):
    """ Информация про книгу"""
    translator = models.CharField(max_length=20)
    publishment_office = models.CharField(max_length=30)
    original_language = models.CharField(max_length=15)
    knowledge_area = models.CharField(max_length=15)
    name = models.CharField(max_length=40)
    author = models.CharField(max_length=20)
    publish_date = models.DateField()

    def __str__(self):
        return self.name


class BookReader(models.Model):
    """ Информация про взятые книги читателем """
    reader = models.ForeignKey('ReaderTicket', on_delete=models.CASCADE, related_name='books')
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='readers_history')
    deadline = models.DateTimeField()

# Сериализаторы

from rest_framework import serializers
from django.contrib.auth import get_user_model

from library.models import (
    Book,
    BookStorageLocation,
    Library,
    Librarian,
    ReaderTicket,
    Reader,
    BookReader
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователя """
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        ref_name = 'User custom'
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password')


class BookSerializer(serializers.ModelSerializer):
    """ Сериализатор книги """
    locations = serializers.SerializerMethodField()

    def get_locations(self, book: Book) -> dict or None:
        location = BookStorageLocation.objects.filter(book=book)
        if not location.exists(): return None

        serialized_data = BookStorageLocationSerializer(location, many=True).data
        return serialized_data

    class Meta:
        model = Book
        fields = [
            'id', 'name', 'author', 'publish_date', 'translator',
            'publishment_office', 'original_language',
            'knowledge_area', 'locations'
        ]


class BookStorageLocationSerializer(serializers.ModelSerializer):
    """ Сериализатор местонахождения книги """
    class Meta:
        model = BookStorageLocation
        fields = '__all__'


class LibrarySerializer(serializers.ModelSerializer):
    """ Сериализатор библиотеки """
    librarians = serializers.SerializerMethodField()
    reader_tickets = serializers.SerializerMethodField()

    def get_librarians(self, library: Library) -> dict:
        librarians = Librarian.objects.filter(library=library)
        serialized_data = LibrarianSerializer(librarians, many=True).data
        return serialized_data

    def get_reader_tickets(self, library: Library) -> dict:
        reader_tickets = ReaderTicket.objects.filter(library=library)
        serialized_data = ReaderTicketSerializer(reader_tickets, many=True).data
        return serialized_data

    class Meta:
        model = Library
        fields = ['id', 'name', 'librarians', 'reader_tickets']


class ReaderSerializer(serializers.ModelSerializer):
    """ Сериализатор читателя """
    class Meta:
        model = Reader
        fields = '__all__'


class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'


class ReaderTicketSerializer(serializers.ModelSerializer):
    books_history = serializers.SerializerMethodField()

    def get_books_history(self, ticket: ReaderTicket) -> dict:
        book_ids = BookReader.objects.filter(reader=ticket).values("book")
        books = Book.objects.filter(id__in=book_ids)
        serialized_data = BookSerializer(books, many=True).data
        return serialized_data

    class Meta:
        model = ReaderTicket
        fields = [
            'id', 'owner', 'registration_date',
            'expiration_date', 'books_history',
            'library'
        ]


class ReaderBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReader
        fields = '__all__'


# Вью

from rest_framework import viewsets

from library.models import (
    Book,
    BookStorageLocation,
    Library,
    Reader,
    Librarian,
    ReaderTicket,
    BookReader
)
from library.serializers import (
    BookSerializer,
    BookStorageLocationSerializer,
    LibrarySerializer,
    ReaderSerializer,
    LibrarianSerializer,
    ReaderTicketSerializer,
    ReaderBooksSerializer
)
from library.permissions import AdminOrReadOnly


class BooksViewsSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AdminOrReadOnly,)


class StorageBooksViewSet(viewsets.ModelViewSet):
    queryset = BookStorageLocation.objects.all()
    serializer_class = BookStorageLocationSerializer
    permission_classes = (AdminOrReadOnly,)


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = (AdminOrReadOnly,)


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes = (AdminOrReadOnly,)


class LibrarianViewSet(viewsets.ModelViewSet):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    permission_classes = (AdminOrReadOnly,)


class ReadTicketViewSet(viewsets.ModelViewSet):
    queryset = ReaderTicket.objects.all()
    serializer_class = ReaderTicketSerializer
    permission_classes = (AdminOrReadOnly,)


class BookReaderViewSet(viewsets.ModelViewSet):
    queryset = BookReader.objects.all()
    serializer_class = ReaderBooksSerializer
    permission_classes = (AdminOrReadOnly,)

# Админ


from django.contrib import admin

from library.models import (
    Library,
    Librarian,
    Reader,
    User,
    Book,
    BookStorageLocation,
    BookReader,
    ReaderTicket,
)


admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(Reader)
admin.site.register(User)
admin.site.register(Book)
admin.site.register(BookStorageLocation)
admin.site.register(BookReader)
admin.site.register(ReaderTicket)


