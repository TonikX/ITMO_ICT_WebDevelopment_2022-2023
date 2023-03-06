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
