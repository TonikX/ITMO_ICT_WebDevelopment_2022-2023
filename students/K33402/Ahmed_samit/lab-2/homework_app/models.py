from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.dispatch import receiver


class Homework(models.Model):
    homework_id = models.IntegerField(blank=False, primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    task = models.CharField(max_length=300)
    subject = models.CharField(max_length=30, blank=False)
    begin_date = models.DateField(blank=False)
    deadline = models.DateField(blank=False)
    penalty = models.CharField(max_length=100)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    students = models.ManyToManyField('Student', through='Assignment')

    def __str__(self):
        return self.name


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #REQUIRED_FIELDS = ['self.user.first_name', 'self.user.last_name']
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Assignment(models.Model):
    assignment_id = models.IntegerField(blank=False, primary_key=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    homework = models.ForeignKey('Homework', on_delete=models.CASCADE)
    grade = models.CharField(default='-', max_length=5, blank=True)
    submission = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.student.user.first_name} {self.student.user.last_name}:\
        {self.homework.name}\
        | {"graded" if self.grade != "-" else "submitted" if len(self.submission) else "in process"}'


@receiver(models.signals.post_save, sender=Homework)
def execute_after_save(sender, instance, created, *args, **kwargs):
    if created:
        students = Student.objects.all()
        for student in students:
            duplicates = Assignment.objects.filter(student=student, homework=instance).all()
            if not len(duplicates):
                assignment = Assignment(student=student, homework=instance)
                assignment.save()

# Create your models here.
