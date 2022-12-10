from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    address = models.CharField("description", max_length=200, null=True)
    age = models.IntegerField("age")
    sex = models.CharField("sex")
    role = models.CharField("role", max_length=200, null=True)
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.username


class School_class(models.Model):
    class_name = models.CharField("class_name", max_length=30, null=False)


class Student_class_teacher(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    class_id = models.ForeignKey('School_class', on_delete=models.CASCADE)
    time = models.DateTimeField()
