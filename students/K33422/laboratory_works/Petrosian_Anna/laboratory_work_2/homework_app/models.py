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
    teacher = models.CharField(max_length=30, blank=False)
    students = models.ManyToManyField('Student', through='Assignment')

    def __str__(self):
        return self.name


class Student(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Assignment(models.Model):
    assignment_id = models.IntegerField(blank=False, primary_key=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    homework = models.ForeignKey('Homework', on_delete=models.CASCADE)
    grade = models.CharField(default='-', max_length=5, blank=True)
    submission = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.student.first_name} {self.student.last_name}:\
        {self.homework.name}\
        | {"graded" if self.grade != "-" else "submitted" if len(self.submission) else "in process"}'


@receiver(models.signals.post_save, sender=Homework)
def execute_after_save(sender, instance, created, *args, **kwargs):
    if created:
        students = Student.objects.exclude(username="teacher").all()
        for student in students:
            duplicates = Assignment.objects.filter(student=student, homework=instance).all()
            if not len(duplicates):
                assignment = Assignment(student=student, homework=instance)
                assignment.save()

# Create your models here.
