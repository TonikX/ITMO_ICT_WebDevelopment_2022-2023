from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

from djangolab3_project import settings


class User(AbstractUser):
	REQUIRED_FIELDS = ["first_name", "last_name"]


# User profiles

class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True,
	                            related_name="%(class)s")

	class Meta:
		abstract = True


class Author(UserProfile):
	pseudonym = models.TextField()


class Manager(UserProfile):
	pass


class Editor(UserProfile):
	pass


class Customer(UserProfile):
	pass


# Books

class Book(models.Model):
	name = models.TextField()
	main_editor = models.ForeignKey(Editor, on_delete=models.CASCADE, related_name="main_editor_books")
	pages = models.IntegerField(default=0)
	authors = models.ManyToManyField(Author, related_name="books", through="BookAuthorship")
	editors = models.ManyToManyField(Editor, related_name="books", through="BookEditorship")
	illustrated = models.BooleanField(default=False)


class BookAuthorship(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="authorships")
	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="authorships")
	priority = models.IntegerField(default=0)


class BookEditorship(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	editor = models.ForeignKey(Editor, on_delete=models.CASCADE)


# Order

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")


class Contract(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="contracts")
	book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="contracts")
	manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name="contracts", null=True, blank=True)
	creation_datetime = models.DateTimeField(default=datetime.now, blank=True)
