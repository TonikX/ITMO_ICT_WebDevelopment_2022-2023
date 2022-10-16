from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .decorators import student_required, teacher_required, allowed_users, additional_info_check
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm, TeacherForm, StudentForm, TeacherAnswerOnHomework, MakeHomeworkForm, CreateHomeworkForm
from .models import Homework, Teacher, Student, StudentGroup, HomeworkAnswer


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


@login_required()
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


@login_required(login_url='login')
@additional_info_check()
def home(request):
    context = {}
    if request.user.is_teacher:
        teacher = Teacher.objects.get(user=request.user)
        homeworks = Homework.objects.filter(teacher=teacher)
        context = {"homeworks": homeworks}
    if request.user.is_student:
        student = Student.objects.get(user=request.user)
        completed_words = HomeworkAnswer.objects.all()
        completed_words = [work.homework for work in completed_words]
        homeworks = Homework.objects.filter(student_group=student.student_group)
        homeworks = [homework for homework in homeworks if homework not in completed_words]
        context = {"homeworks": homeworks}
    return render(request, "pages/home.html", context)


@teacher_required()
def teacher_marks_page(request):
    if request.method == "POST":
        form = TeacherAnswerOnHomework(request.POST)
        if form.is_valid():
            points = form.cleaned_data['points']
            message = form.cleaned_data['message']
            homework_answer_id = form.cleaned_data["homework_answer_id"]
            homework_answer = HomeworkAnswer.objects.get(pk=homework_answer_id)
            homework_answer.teacher_message = message
            homework_answer.points = points
            homework_answer.save()
    teacher = Teacher.objects.get(user=request.user)
    homeworks = Homework.objects.filter(teacher=teacher)
    answers = []
    for homework in homeworks:
        answer = HomeworkAnswer.objects.get(homework=homework)
        points = answer.points
        form = TeacherAnswerOnHomework(points=points, homework_answer=answer, message=answer.teacher_message)
        answers.append({"answer": answer, "form": form})
    context = {"answers": answers}
    return render(request, 'pages/marks.html', context)


@student_required()
def student_marks_page(request):
    student = Student.objects.get(user=request.user)
    homeworks = Homework.objects.filter(student_group=student.student_group)
    answers = []
    for homework in homeworks:
        answer = HomeworkAnswer.objects.get(homework=homework)
        points = answer.points
        answers.append({"answer": answer, "points": points})
    context = {"answers": answers}
    print(answers)
    return render(request, 'pages/marks.html', context)


def make_homework(request, work_id):
    homework = Homework.objects.get(pk=work_id)
    student = Student.objects.get(user=request.user)
    homework_answer = HomeworkAnswer.objects.get_or_create(homework=homework, student=student)[0]
    if request.method == "POST":
        form = MakeHomeworkForm(request.POST)
        if form.is_valid():
            print("DATA", form.cleaned_data)
            homework_answer.answer = form.cleaned_data["answer"]
            homework_answer.points = 0
            homework_answer.teacher_message = ""
            homework_answer.save()
            return redirect("marks")
    form = MakeHomeworkForm(answer=homework_answer.answer, homework=homework)
    context = {"word_id": work_id, "form": form, "homework": homework}
    return render(request, 'pages/make_homework.html', context)


def create_homework(request, work_id):
    homework = Homework.objects.get_or_create(pk=work_id)[0]
    if request.method == "POST":
        form = CreateHomeworkForm(request.POST, instance=homework, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
    form = CreateHomeworkForm(instance=homework, user=request.user)
    context = {"word_id": work_id, "form": form, "homework": homework}
    return render(request, 'pages/create_homework.html', context)

@login_required()
def marks(request):
    if request.user.is_teacher:
        return redirect('teacher_marks')
    if request.user.is_student:
        return redirect('student_marks')


def logoutUser(request):
    logout(request)
    return redirect('login')
