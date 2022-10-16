from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .decorators import student_required, teacher_required, allowed_users
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm, TeacherForm, StudentForm


def registerPage(requset):
    form = RegisterForm

    if requset.method == "POST":
        form = RegisterForm(requset.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(requset, 'register.html', context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}

    return render(request, 'login.html', context)


def add_info(request):
    if request.user.is_teacher:
        if request.method == "POST":
            form = TeacherForm(request.POST, user=request.user)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = TeacherForm(_user=request.user)
            context = {"form": form}
            return render(request, "add_info.html", context)
    if request.user.is_student:
        if request.method == "POST":
            form = StudentForm(request.POST, user=request.user)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = StudentForm(user=request.user)
            context = {"form": form}
            return render(request, "add_info.html", context)
    # if request.user.is_student:


@student_required()
def home(request):
    # if not request.user.with_additional_info:
    #     return redirect("add_info")
    return render(request, "home.html")


@student_required()
def for_student(response):
    print('Hello student!!!')
