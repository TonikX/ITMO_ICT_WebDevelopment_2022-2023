# Лабораторная работа 2

## Описание задачи

### *Доска домашних заданий*

О домашнем задании должна храниться следующая информация: предмет,
преподаватель, дата выдачи, период выполнения, текст задания, информация о штрафах.
Необходимо реализовать следующий функционал:
- Регистрация новых пользователей.
- Просмотр домашних заданий по всем дисциплинам (сроки выполнения,
описание задания).
- Сдача домашних заданий в текстовом виде.
- Администратор (учитель) должен иметь возможность поставить оценку за
задание средствами Django-admin.
- В клиентской части должна формироваться таблица, отображающая оценки
всех учеников класса.

## Видео

https://www.youtube.com/watch?v=Ta3NmCC-Hn4

## Структура проекта

```
.
├── laboratory_work_2
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates
│   ├── components
│   │   ├── header.html
│   │   ├── homework.html
│   │   ├── homework_answer.html
│   │   ├── homework_answers_album.html
│   │   └── homeworks_album.html
│   ├── pages
│   │   ├── add_info.html
│   │   ├── create_homework.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── make_homework.html
│   │   ├── marks.html
│   │   ├── rate_homework.html
│   │   ├── register.html
│   │   └── task_answer.html
│   └── base.html
├── timetable
│   ├── migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── decorators.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
└── manage.py
```

## Листинги

### `model.py`

```python
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
    ("Математика", "Математика"),
    ("История", "История"),
    ("ИЗО", "ИЗО"),
    ("Русский язык", "Русский язык"),
    ("География", "География")
]


class StudentGroup(models.Model):
    character = models.CharField(max_length=1, choices=CHARACTERS, default="A", verbose_name="Литера")
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
```

### `decorators.py`

```python
def student_required():
    def decorator(view_func):
        def wrapper_func(requset, *args, **kwargs):
            if requset.user.is_student:
                return view_func(requset, *args, **kwargs)
            else:
                return HttpResponse('You are not student')

        return wrapper_func

    return decorator


def additional_info_check():
    def decorator(view_func):
        def wrapper_func(requset, *args, **kwargs):
            if requset.user.with_additional_info:
                return view_func(requset, *args, **kwargs)
            else:
                return redirect("add_info")

        return wrapper_func

    return decorator


def teacher_required():
    def decorator(view_func):
        def wrapper_func(requset, *args, **kwargs):
            if requset.user.is_teacher:
                return view_func(requset, *args, **kwargs)
            else:
                return HttpResponse('You are not teacher')

        return wrapper_func

    return decorator

```

### `forms.py`

```python
groups = [(group.pk, group) for group in StudentGroup.objects.all()]


class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(
        required=True,
        choices=ROLES
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        print("ROLE", self.cleaned_data["role"])
        if self.cleaned_data["role"] == "teacher":
            user.is_teacher = True
        if self.cleaned_data["role"] == "student":
            user.is_student = True
        if commit:
            user.save()
        return user


class TeacherForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TeacherForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Teacher
        fields = ["subject"]

    def save(self, commit=True):
        teacher = super(TeacherForm, self).save(commit=False)
        teacher.user = self.user
        teacher.user.with_additional_info = True
        if commit:
            teacher.user.save()
            teacher.save()
        return teacher


class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(StudentForm, self).__init__(*args, **kwargs)

    student_group = forms.ChoiceField(required=True, choices=groups)

    class Meta:
        model = Student
        fields = ["student_group"]

    def save(self, commit=True):
        student = super(StudentForm, self).save(commit=False)
        student.user = self.user
        student.user.with_additional_info = True
        student.student_group = StudentGroup.objects.get(pk=self.cleaned_data["student_group"])
        if commit:
            student.user.save()
            student.save()
        return student


class TeacherAnswerOnHomeworkForm(forms.ModelForm):
    class Meta:
        model = TeacherAnswerOnHomework
        fields = ["points", "message"]

    def __init__(self, *args, **kwargs):
        self.homework_answer = kwargs.pop('homework_answer', None)
        super(TeacherAnswerOnHomeworkForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        teacher_homework_answer = super(TeacherAnswerOnHomeworkForm, self).save(commit=False)
        teacher_homework_answer.homework_answer = self.homework_answer
        if commit:
            teacher_homework_answer.save()
        return teacher_homework_answer


class HomeworkAnswerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.homework = kwargs.pop('homework', None)
        self.student = kwargs.pop('student', None)
        super(HomeworkAnswerForm, self).__init__(*args, **kwargs)

    class Meta:
        model = HomeworkAnswer
        fields = ["answer"]

    answer = forms.CharField(label='message', max_length=180)

    def save(self, commit=True):
        homework_answer = super(HomeworkAnswerForm, self).save(commit=False)
        homework_answer.homework = self.homework
        homework_answer.student = self.student
        if commit:
            homework_answer.save()
        return homework_answer


class HomeworkForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(HomeworkForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Homework
        fields = ["task_description", "start_date", "end_date", "max_points", "fine_info"]
        widgets = {
            "start_date": forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            "end_date": forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'})
        }

    student_group = forms.ChoiceField(required=True, choices=groups)

    def save(self, commit=True):
        homework = super(HomeworkForm, self).save(commit=False)
        homework.student_group = StudentGroup.objects.get(pk=self.cleaned_data["student_group"])
        homework.teacher = Teacher.objects.get(user=self.user)
        homework.subject = homework.teacher.subject
        if commit:
            homework.save()
        return homework

```


### `views.py`

```python
import django.db
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import student_required, teacher_required, additional_info_check
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm, TeacherForm, StudentForm, HomeworkAnswerForm, HomeworkForm, \
    TeacherAnswerOnHomeworkForm
from .models import Homework, Teacher, Student, HomeworkAnswer, TeacherAnswerOnHomework


def registerPage(requset):
    form = RegisterForm

    if requset.method == "POST":
        form = RegisterForm(requset.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(requset, 'pages/register.html', context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}

    return render(request, 'pages/login.html', context)


@login_required(login_url='login')
def add_info(request):
    if request.user.is_teacher:
        if request.method == "POST":
            form = TeacherForm(request.POST, user=request.user)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = TeacherForm(user=request.user)
            context = {"form": form}
            return render(request, "pages/add_info.html", context)

    if request.user.is_student:
        if request.method == "POST":
            form = StudentForm(request.POST, user=request.user)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = StudentForm(user=request.user)
            context = {"form": form}
            return render(request, "pages/add_info.html", context)
    return HttpResponse("You are not teacher or student")


@login_required(login_url='login')
@additional_info_check()
def home(request):
    if request.user.is_teacher:
        return redirect("teacher_home")
    if request.user.is_student:
        return redirect("student_home")
    return HttpResponse("You are not teacher or student")


def get_checked_and_unchecked_homeworks(homeworks):
    checked_homeworks = []
    unchecked_homeworks = []
    for homework in homeworks:
        try:
            t = homework.teacheransweronhomework
            if t:
                checked_homeworks.append(homework)
        except TeacherAnswerOnHomework.DoesNotExist:
            unchecked_homeworks.append(homework)
    return {"checked_homeworks": checked_homeworks, "unchecked_homeworks": unchecked_homeworks}


@login_required(login_url='login')
@teacher_required()
def teacher_marks_page(request):
    homeworks = Homework.objects.filter(teacher=request.user.teacher)
    homework_answers = []
    for homework in homeworks:
        try:
            homework_answers.append(HomeworkAnswer.objects.get(homework=homework))
        except HomeworkAnswer.DoesNotExist:
            continue

    filtered_homeworks = get_checked_and_unchecked_homeworks(homework_answers)
    context = {"homework_answers": homework_answers, "checked_homeworks": filtered_homeworks["checked_homeworks"],
               "unchecked_homeworks": filtered_homeworks["unchecked_homeworks"]}
    return render(request, 'pages/marks.html', context)


@login_required(login_url='login')
@student_required()
def student_marks_page(request):
    student = Student.objects.get(user=request.user)
    homeworks = Homework.objects.filter(student_group=student.student_group)
    homework_answers = []
    for homework in homeworks:
        try:
            homework_answers.append(HomeworkAnswer.objects.get(homework=homework))
        except HomeworkAnswer.DoesNotExist:
            continue

    filtered_homeworks = get_checked_and_unchecked_homeworks(homework_answers)
    context = {"homework_answers": homework_answers, "checked_homeworks": filtered_homeworks["checked_homeworks"],
               "unchecked_homeworks": filtered_homeworks["unchecked_homeworks"]}
    return render(request, 'pages/marks.html', context)


@login_required(login_url='login')
@teacher_required()
def delete_homework(request, work_id):
    homework = Homework.objects.get(pk=work_id)
    homework.delete()
    return redirect("home")


@login_required(login_url='login')
@teacher_required()
def change_homework(request, work_id):
    homework = Homework.objects.get_or_create(pk=work_id)[0]
    if request.method == "POST":
        form = HomeworkForm(request.POST, instance=homework, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
    form = HomeworkForm(instance=homework, user=request.user)
    context = {"word_id": work_id, "form": form, "homework": homework}
    return render(request, 'pages/create_homework.html', context)


@login_required(login_url='login')
@teacher_required()
def create_homework(request):
    if request.method == "POST":
        form = HomeworkForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
    form = HomeworkForm(user=request.user)
    context = {"form": form}
    return render(request, 'pages/create_homework.html', context)


@login_required(login_url='login')
@teacher_required()
def teacher_home_page(request):
    teacher = Teacher.objects.get(user=request.user)
    homeworks = Homework.objects.filter(teacher=teacher)
    context = {"homeworks": homeworks}
    return render(request, "pages/home.html", context)


@login_required(login_url='login')
@student_required()
def student_home_page(request):
    student = Student.objects.get(user=request.user)
    completed_words = HomeworkAnswer.objects.all()
    completed_words = [work.homework for work in completed_words]
    homeworks = Homework.objects.filter(student_group=student.student_group)
    homeworks = [homework for homework in homeworks if homework not in completed_words]
    context = {"homeworks": homeworks}
    return render(request, "pages/home.html", context)


@login_required(login_url='login')
@login_required()
def marks(request):
    if request.user.is_teacher:
        return redirect('teacher_marks')
    if request.user.is_student:
        return redirect('student_marks')


@login_required(login_url='login')
@teacher_required()
def rate_homework(request, work_id):
    try:
        homework_answer = HomeworkAnswer.objects.get(pk=work_id)
    except HomeworkAnswer.DoesNotExist:
        return HttpResponse("Homework answer does not exist")

    try:
        if request.method == "POST":
            form = TeacherAnswerOnHomeworkForm(request.POST, instance=homework_answer.teacheransweronhomework,
                                               homework_answer=homework_answer)
            if form.is_valid():
                form.save()
                return redirect("marks")
        form = TeacherAnswerOnHomeworkForm(instance=homework_answer.teacheransweronhomework,
                                           homework_answer=homework_answer)
        context = {"form": form, "homework_answer": homework_answer}
        return render(request, 'pages/rate_homework.html', context)
    except TeacherAnswerOnHomework.DoesNotExist:
        if request.method == "POST":
            form = TeacherAnswerOnHomeworkForm(request.POST, homework_answer=homework_answer)
            if form.is_valid():
                form.save()
                return redirect("marks")
        form = TeacherAnswerOnHomeworkForm(homework_answer=homework_answer)
        context = {"form": form, "homework_answer": homework_answer}
        return render(request, 'pages/rate_homework.html', context)


@login_required(login_url='login')
@student_required()
def make_homework(request, work_id):
    student = Student.objects.get(user=request.user)

    try:
        homework = Homework.objects.get(pk=work_id)
    except Homework.DoesNotExist:
        return HttpResponse("Homework answer does not exist")

    if request.method == "POST":
        form = HomeworkAnswerForm(request.POST, homework=homework, student=student)
        if form.is_valid():
            form.save()
            return redirect("marks")
    form = HomeworkAnswerForm(homework=homework, student=student)
    context = {"form": form, "homework": homework}
    return render(request, 'pages/make_homework.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')
```