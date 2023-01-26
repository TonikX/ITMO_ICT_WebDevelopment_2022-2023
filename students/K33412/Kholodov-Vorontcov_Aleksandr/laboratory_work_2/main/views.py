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
