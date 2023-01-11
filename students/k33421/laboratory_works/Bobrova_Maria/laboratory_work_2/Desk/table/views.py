from django.shortcuts import render

# Create your views here.
import django.db
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
                                               homework_answer=homework_answer, user=request.user)
            if form.is_valid():
                form.save()
                return redirect("marks")
        form = TeacherAnswerOnHomeworkForm(instance=homework_answer.teacheransweronhomework,
                                           homework_answer=homework_answer, user=request.user)
        context = {"form": form, "homework_answer": homework_answer}
        return render(request, 'pages/rate_homework.html', context)
    except TeacherAnswerOnHomework.DoesNotExist:
        if request.method == "POST":
            form = TeacherAnswerOnHomeworkForm(request.POST, homework_answer=homework_answer, user=request.user)
            if form.is_valid():
                form.save()
                return redirect("marks")
        form = TeacherAnswerOnHomeworkForm(homework_answer=homework_answer, user=request.user)
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