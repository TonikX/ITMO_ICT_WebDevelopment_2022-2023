from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    with_additional_info = models.BooleanField(default=False)


CHARACTERS = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C')
]

NUMBERS = [
    (1, '1'),
    (2, '2'),
    (3, '3')
]

SUBJECTS = [
    ("Math", "Math"),
    ("History", "History"),
    ("Art", "Art"),
    ("English", "English")
]


class StudentGroup(models.Model):
    character = models.CharField(max_length=1, choices=CHARACTERS, default="A")
    number = models.IntegerField(choices=NUMBERS, default=1)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, null=True)
    birthdate = models.DateField()


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    subject = models.CharField(max_length=30, choices=SUBJECTS)


class Homework(models.Model):
    student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=30, choices=SUBJECTS)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    task_description = models.TextField()
    fine_info = models.CharField(max_length=150)
    max_points = models.IntegerField()


class HomeworkAnswer(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, blank=True)
    points = models.IntegerField(default=0, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    teacher_message = models.TextField(null=True, blank=True)

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
