# Лабораторная работа №2
Реализовать сайт используя фреймворк Django 3
## Вариант 2
### Доска домашних заданий
О домашнем задании должна храниться следующая информация: предмет,
преподаватель, дата выдачи, период выполнения, текст задания, информация о штрафах.
### Функционал
* Регистрация новых пользователей.
* Просмотр домашних заданий по всем дисциплинам.
* Сдача домашних заданий в текстовом виде.
* Учитель может поставить оценку за
задание в Django-admin.
* Таблица, отображающая оценки всех учеников класса по всем заданиям.

### Структура
`lab2_Barysheva` - проект Django

`homework_board` - приложение Django 

### Проект Django
Обьявленная модель пользователя и приложения в `settings.py`
```
AUTH_USER_MODEL = "homework_board.User"
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "homework_board",
]
```
Паттерны url в `urls.py`
```
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('homework_board.urls')),
]
```

### Приложение Django
Паттерны url в `urls.py`
```
urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('report_card/', get_report_card),
    path('assignments/', get_all_tasks),
    path('assignments/<int:task_id>/', get_task),
    path('assignments/<int:task_id>/send/', send_new_donetask),
    path('reg/', create_new_user, name='reg'),
    path('assignments/create/', create_new_task),
    path('exit/', exit),
]
```

Модели в `models.py`
```
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

```

Формы в `forms.py`
```
class DoneTaskForm(ModelForm):
    class Meta:
        model = DoneTask
        fields = ['text']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'surname', 'name', 'password']

class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['subject_id', 'start_date', 'end_date', 'text', 'fine']

```

Представления в `views.py`
```
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import DoneTaskForm, UserForm, AssignmentForm

from homework_board.models import *

@login_required()
def get_report_card(request):
        tasks = Assignment.objects.all()
        students = User.objects.filter(is_teacher=0)
        report_card = {}

        for student in students:
            student_marks_dict = {}
            for task in tasks:
                try:
                    student_task = DoneTask.objects.get(assignment_id=task.pk, student_id=student.pk)
                    student_mark = student_task.mark
                except DoneTask.DoesNotExist:
                    student_mark = 0
                student_marks_dict[task.pk] = student_mark
            report_card[str(student.surname) + ' ' + str(student.name) + ' (' + str(student.pk) + ')'] = student_marks_dict
        return render(request, 'report_card.html', {'report_card': report_card, 'tasks': tasks})

@login_required()
def get_all_tasks(request):
     check = request.user.is_teacher
     tasks_list = Assignment.objects.all()
     return render(request, 'assignments_list.html', {'tasks_list': tasks_list, 'check': check})

@login_required()
def send_new_donetask(request, task_id):
    if request.method == 'POST':
        form = DoneTaskForm(request.POST)
        if form.is_valid():
            new_done_task = form.save(commit=False)
            new_done_task.student_id = request.user
            new_done_task.assignment_id = Assignment.objects.get(pk=task_id)
            new_done_task.save()
        return HttpResponseRedirect('/report_card/')
    else:
        form = DoneTaskForm()

    return render(request, 'done_task.html', {'form': form, 'task_id': task_id})

            
def create_new_user(request):          
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
        return HttpResponseRedirect('/report_card/')
    else:
        form = UserForm()

    return render(request, 'reg_student.html', {'form': form})

@login_required()
def create_new_task(request): 
    check = request.user.is_teacher
    if check:         
        if request.method == 'POST':
            form = AssignmentForm(request.POST)
            if form.is_valid():
                new_assignment = form.save(commit=False)
                new_assignment.teacher_id = request.user
                new_assignment.save()
            return HttpResponseRedirect('/assignments/')
        else:
            form = AssignmentForm()
    else:
        return HttpResponseRedirect('/report_card/')
    return render(request, 'create_assignment.html', {'form': form})


@login_required()
def exit(request):
    logout(request)

@login_required()
def get_task(request, task_id):
     task = Assignment.objects.get(pk=task_id)
     return render(request, 'assignment.html', {'task': task})
```
