from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Student(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Homework(models.Model):
    name = models.CharField(max_length=50, blank=False)
    subject = models.CharField(max_length=30, blank=False)
    teacher = models.CharField(max_length=30, blank=False)
    post_date = models.DateField(blank=False)
    deadline = models.DateField(blank=False)
    task = models.CharField(max_length=1000)
    students = models.ManyToManyField('Student', through='Assignment')

    def __str__(self):
        return self.name


class Assignment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    homework = models.ForeignKey('Homework', on_delete=models.CASCADE)
    submission = models.CharField(max_length=1000, blank=True)
    grade = models.CharField(default='none', max_length=5, blank=True)

    def __str__(self):
        return f'{self.homework.name} {self.student.last_name}'
