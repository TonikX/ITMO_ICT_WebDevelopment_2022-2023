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
		return 'Comment {} by {}'.format(self.body, self.author.username)
