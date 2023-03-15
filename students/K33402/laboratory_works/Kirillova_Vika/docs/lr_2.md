# Лабораторная работа №2 - Реализация простого сайта на django 

## Цель 
* Овладеть практическими навыками и умениями реализации web-сервисов средствами Django.
## Используемое ПО
* Python 3.10, Django 3.
## Описание задачи:
### Доска домашних заданий
О домашнем задании должна храниться следующая информация: предмет, преподаватель, дата выдачи, период выполнения, текст задания, информация о штрафах. 

## Необходимо реализовать следующий функционал: 
* Регистрация новых пользователей. 
* Просмотр домашних заданий по всем дисциплинам (сроки выполнения, описание задания).
* Сдача домашних заданий в текстовом виде. 
* Администратор (учитель) должен иметь возможность поставить оценку за задание средствами Django-admin.
* В клиентской части должна формироваться таблица, отображающая оценки всех учеников класса.

## Листинги

* `models.py`
```python
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.dispatch import receiver


class Homework(models.Model):
    homework_id = models.IntegerField(blank=False, primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=30, blank=False)
    teacher = models.CharField(max_length=30, blank=False)
    begin_date = models.DateField(blank=False)
    deadline = models.DateField(blank=False)
    task = models.CharField(max_length=1000)
    penalty = models.CharField(max_length=100)
    students = models.ManyToManyField('Student', through='Assignment')

    def __str__(self):
        return self.name


class Assignment(models.Model):
    assignment_id = models.IntegerField(blank=False, primary_key=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    homework = models.ForeignKey('Homework', on_delete=models.CASCADE)
    grade = models.CharField(default='-', max_length=5, blank=True)
    submission = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f'{self.student.first_name} {self.student.last_name}:\
        {self.homework.name}\
        | {"graded" if self.grade != "-" else "submitted" if len(self.submission) else "in process"}'


class Student(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


@receiver(models.signals.post_save, sender=Homework)
def execute_after_save(sender, instance, created, *args, **kwargs):
    if created:
        students = Student.objects.exclude(username="teacher").all()
        for student in students:
            duplicates = Assignment.objects.filter(student=student, homework=instance).all()
            if not len(duplicates):
                assignment = Assignment(student=student, homework=instance)
                assignment.save()

```

* `forms.py`
```python
from django import forms
from main.models import Assignment


class AssignmentForm(forms.ModelForm):
    submission = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Assignment
        fields = ['submission']

```

 * `views.py`
```python
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from main.models import Student, Homework, Assignment
from main.forms import AssignmentForm


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        first_name = request.POST.get("first_name", 'NaN')
        last_name = request.POST.get("last_name", 'NaN')

        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "passwords do not match"
            })

        try:
            student = Student.objects.create_user(username, email, password)
            student.first_name = first_name
            student.last_name = last_name
            student.save()
            homeworks = Homework.objects.all()
            for homework in homeworks:
                assignment = Assignment(student=student, homework=homework)
                assignment.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "username already taken"
            })
        login(request, student)
        return redirect(reverse("homework_list"))
    else:
        return render(request, "register.html")


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('homework_list'))
        else:
            error_text = 'invalid credentials'

    return render(request, 'login.html', locals())


@login_required
def log_out(request):
    logout(request)
    return redirect(reverse('login'))


@login_required
def class_grades_list(request):
    context = {}
    students = Student.objects.exclude(username="teacher").all()
    context["students"] = students
    context["homeworks"] = Homework.objects.all()
    context["grades"] = {}
    assignments = Assignment.objects.all()
    for homework in context["homeworks"]:
        for assignment in assignments:
            if assignment.homework == homework and assignment.student.pk != 3:
                if not assignment.student.pk in context["grades"]:
                    context["grades"][assignment.student.pk] = []
                context["grades"][assignment.student.pk].append(
                    assignment.grade)

    return render(request, 'class_grades.html', context)


class HomeworkList(ListView):
    model = Homework
    template_name = 'homework_list.html'


class HomeworkDetail(DetailView):
    model = Homework
    template_name = 'homework_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AssignmentForm()
        return context


@login_required
def hand_in(request, pk):
    homework = Homework.objects.get(pk=pk)
    assignment = Assignment.objects.get(student=request.user,
                                        homework=homework)
    form = AssignmentForm(request.POST, instance=assignment)
    if form.is_valid():
        form.save()

        return redirect(reverse('homework_list'))

```