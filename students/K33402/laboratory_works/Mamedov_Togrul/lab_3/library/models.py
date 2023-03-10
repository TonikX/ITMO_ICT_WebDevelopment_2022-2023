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


class Librarian(User):
    """ Библиотекарь """
    library = models.ForeignKey('Library', on_delete=models.CASCADE, related_name='librarians')


class Library(models.Model):
    """ Библиотека """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


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
