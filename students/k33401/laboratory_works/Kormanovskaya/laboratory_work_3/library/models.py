from django.db import models
from django.db.models import Avg
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Achievement(models.Model):
    """
    Achievements obtained through user actions.
    """
    name = models.CharField('Achievement name', max_length=64, unique=True)
    description = models.TextField('Achievement description')
    points = models.IntegerField()

    def __str__(self):
        return self.name


class UserAchievement(models.Model):
    """
    Binding entity for users and their achievements. Contains the date of receipt.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.user} [{self.date}] - \"{self.achievement}\""


class Author(models.Model):
    name = models.CharField('Author name', max_length=64, unique=True)
    slug = models.SlugField('Author link', max_length=64, unique=True)

    def get_absolute_url(self):
        return reverse('author_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Genre name', max_length=64, unique=True)
    slug = models.SlugField('Genre link', max_length=64, unique=True)

    def get_absolute_url(self):
        return reverse('genre_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField('Book title', max_length=150, db_index=True)
    slug = models.SlugField('Book link', max_length=150, unique=True)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'"{self.title}" {self.author}'

    def get_absolute_url(self):
        return reverse('book_url', kwargs={'slug': self.slug})


class Reading(models.Model):
    """
    The book on the user's shelf. Contains status and feedback.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reading")
    is_read = models.BooleanField(default=False)
    review_text = models.TextField(null=True, default=None, blank=True)
    rate = models.IntegerField(null=True, default=None, blank=True)

    def __str__(self):
        return f"[{'+' if self.is_read else '-'}] {self.book} / {self.user}"
