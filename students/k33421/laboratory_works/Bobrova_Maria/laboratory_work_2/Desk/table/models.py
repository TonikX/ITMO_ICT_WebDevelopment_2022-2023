from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    with_additional_info = models.BooleanField(default=False)


CHARACTERS = [
    ('K', 'K')
]

NUMBERS = [
    (1, '3241'),
    (2, '3242')
]

SUBJECTS = [
    ("Математика", "Математика"),
    ("История", "История"),
    ("КИГ", "КИГ"),
    ("Программирование", "Программирование"),
    ("Информатика", "Информатика")
]


class StudentGroup(models.Model):
    character = models.CharField(max_length=1, choices=CHARACTERS, default="K", verbose_name="Литера")
    number = models.IntegerField(choices=NUMBERS, default=1, verbose_name="Номер")

    def __str__(self):
        return f"{self.character}{self.number}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    subject = models.CharField(max_length=30, choices=SUBJECTS, verbose_name="Предмет")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Homework(models.Model):
    student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=30, choices=SUBJECTS, verbose_name="Предмет")
    start_date = models.DateTimeField(verbose_name="Дата выдачи")
    end_date = models.DateTimeField(verbose_name="Сдать до")
    task_description = models.TextField(verbose_name="Описание")
    fine_info = models.CharField(max_length=150, verbose_name="Информация о штрафах")
    max_points = models.IntegerField(verbose_name="Максимальное количество баллов")


class HomeworkAnswer(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, blank=True)
    answer = models.TextField(null=True, blank=True, verbose_name="Ответ")


class TeacherAnswerOnHomework(models.Model):
    homework_answer = models.OneToOneField(HomeworkAnswer, on_delete=models.CASCADE, primary_key=True)
    points = models.IntegerField(default=0, verbose_name="Баллы")
    message = models.TextField(null=True, blank=True, verbose_name="Сообщение")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=True, blank=True)