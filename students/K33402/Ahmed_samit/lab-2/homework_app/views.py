from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from homework_app.models import Student, Homework, Assignment,User,Teacher
from homework_app.forms import AssignmentForm,StudentSignUpForm,TeacherSignUpForm,HomeworkForm
from homework_app.decorators import student_required,teacher_required
from django.http import HttpResponseRedirect
class StudentSignUpView(CreateView):
        
    model = User
    form_class = StudentSignUpForm
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
   
        user = form.save()
        login(self.request, user)
        return redirect('login')

class TearchSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
   
        user = form.save()
        login(self.request, user)
        return redirect('login')
@method_decorator(teacher_required, name='dispatch')

class HomeworkCreate(CreateView):
    model = Homework 
    form_class: HomeworkForm
    template_name = 'createhomework.html'
    fields = "__all__"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = HomeworkForm()
        return context
    def form_valid(self, form):

        form.save()
        
        return redirect('homework_list')
    



def log_in(request):
    # if request.user.is_authenticated:
    #     return redirect('homework_list')
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
@teacher_required
def class_grades_list(request):
    context = {}
    students = Student.objects.all()
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

@method_decorator(login_required, name='dispatch')

class HomeworkList(ListView):
 
    model = Homework
    template_name = 'homework_list.html'

@method_decorator(login_required, name='dispatch')
class HomeworkDetail(DetailView):
    model = Homework
    template_name = 'homework_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AssignmentForm()
        return context

@method_decorator(student_required, name='dispatch')   

class AssignmentView(ListView):
    model = Assignment
    template_name = 'studentgrade.html'

    def get_queryset(self):
        studentt=Student.objects.get(user=self.request.user)
        return Assignment.objects.filter(student=studentt)


@login_required
def hand_in(request, pk):
    homework = Homework.objects.get(pk=pk)
    studentt = Student.objects.get(user=request.user)
    assignment = Assignment.objects.get(student=studentt,homework=homework)
    form = AssignmentForm(request.POST,instance=assignment)
    if form.is_valid():
        form.save()

        return redirect(reverse('homework_list'))

