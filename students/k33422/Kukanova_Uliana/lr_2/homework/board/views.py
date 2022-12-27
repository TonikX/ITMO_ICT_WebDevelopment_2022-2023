from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from board.models import Student, Homework, Assignment
from board.forms import NewStudent, NewSubmission
# Create your views here.


def find_home(request):
    if request.user.is_authenticated:
        return redirect('/all_hw')
    else:
        return redirect('/login')


def register(request):
    form = NewStudent()
    if request.method == "POST":
        form = NewStudent(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    data = {'form': form}
    return render(request, 'register.html', data)


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/all_hw')

    data = {}
    return render(request, 'login.html', data)


def log_out(request):
    logout(request)
    return redirect('/login')


class AllHomework(ListView):
    model = Homework
    template_name = 'all_hw.html'


class OneHomework(DetailView):
    model = Homework
    template_name = 'hw.html'


class AddSubmission(CreateView):
    form_class = NewSubmission
    model = Assignment
    template_name = 'submit.html'

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)


class OurGrades(ListView):
    model = Assignment
    template_name = 'our_grades.html'
