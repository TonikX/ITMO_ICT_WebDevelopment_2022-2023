from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=12)


class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=20, null=True)


class Homework(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    is_work_submitted = models.BooleanField(default=False)
    task_description = models.CharField(max_length=100, null=True)
    date_start = models.DateTimeField(null=True)
    date_end = models.DateTimeField(null=True)


class Grade(models.Model):
    grade = models.IntegerField(null=True, blank=True)
    homework = models.ForeignKey(Homework, null=True, on_delete=models.CASCADE)
