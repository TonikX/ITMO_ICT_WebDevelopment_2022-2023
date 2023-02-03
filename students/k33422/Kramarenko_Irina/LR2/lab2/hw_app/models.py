from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
# from datetime import datetime


class TeacherHomework(models.Model):
    subject = models.CharField(max_length=20)
    study_class = models.CharField(max_length=3, blank=True)
    date_start = models.DateField()
    date_end = models.DateField()
    info = models.CharField(max_length=1000, blank=True)


class Student(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField(null=True)
    study_class = models.CharField(max_length=3, blank=True)
    case = models.ManyToManyField(TeacherHomework, through='StudentHomework')


class StudentHomework(models.Model):
    TYPE_G = ((5, 5), (4, 4), (3, 3), (2, 2))
    student_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    homework_id = models.ForeignKey(TeacherHomework, on_delete=models.DO_NOTHING)
    date_submit = models.DateField(default=timezone.now)
    text = models.CharField(max_length=1000, blank=True)
    grade = models.IntegerField(choices=TYPE_G, null=True, blank=True)