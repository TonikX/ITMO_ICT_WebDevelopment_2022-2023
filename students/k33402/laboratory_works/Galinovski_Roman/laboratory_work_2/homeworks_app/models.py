from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    TYPE_EX = (
        ('teacher', 'я учитель'),
        ('student', 'я студент'))
    status = models.CharField(max_length=10, null=True, blank=True, choices=TYPE_EX)
    group = models.CharField(max_length=10, null=True, blank=True)


class Course(models.Model):
    course_name = models.CharField(max_length=20)


class Homework(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    period = models.IntegerField(null=True, blank=True) 
    task = models.TextField(null=True, blank=True)
    fine_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title + '(' + self.teacher.first_name + ')' + ' @' + self.course.course_name


class StudentHomework(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    mark = models.IntegerField(null=True, blank=True)
    done_task = models.TextField(null=True, blank=True)