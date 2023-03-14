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