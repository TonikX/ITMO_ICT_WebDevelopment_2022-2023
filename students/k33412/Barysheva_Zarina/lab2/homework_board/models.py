from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    is_teacher = models.BooleanField(default=False)
    

class Subject(models.Model):
    teacher_id = models.ForeignKey(User,on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=30)


class Assignment(models.Model):
    teacher_id = models.ForeignKey(User,on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.datetime.now())
    end_date = models.DateField()
    text = models.CharField(max_length=500)
    fine = models.CharField(max_length=500)

class DoneTask(models.Model):
    assignment_id = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    student_id = models.ForeignKey(User,on_delete=models.CASCADE)
    done_date = models.DateField(default=datetime.datetime.now())
    text = models.CharField(max_length=500)
    mark = models.CharField(max_length=5, default=0)

