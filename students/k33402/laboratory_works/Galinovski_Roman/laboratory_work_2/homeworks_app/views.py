from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from .models import User, Course, Homework, StudentHomework
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.status == 'student':
                        return HttpResponseRedirect('/')
                    else:
                        return HttpResponseRedirect('/admin/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


class UserCreate(CreateView):
    model = User
    template_name = 'registration.html'

    fields = ['username', 'password', 'first_name', 'last_name', 'status', 'group']
    success_url = '/login/'

    def form_valid(self, form):
        self.object = form.save()
        self.object.set_password(form.cleaned_data['password'])

        if self.object.status == 'teacher':
            self.object.is_staff = True
            self.object.is_superuser = True

        self.object.save()

        return HttpResponseRedirect('/login/')


class UserList(ListView):
    model = User
    template_name = 'user_list.html'


class HomeworkList(ListView):
    model = Homework
    template_name = 'homeworks.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect('/login/')

        return super(HomeworkList, self).dispatch(request, *args, **kwargs)


class HomeworkCreate(CreateView):
    model = Homework
    template_name = 'homework_create.html'

    fields = ['title', 'course', 'teacher', 'start_date', 'period', 'task', 'fine_info']


class HomeworkUpload(CreateView):
    model = StudentHomework
    template_name = 'homework_upload.html'

    fields = ['homework', 'done_task']
    success_url = '/'

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)


class HomeworkMark(DetailView, UpdateView):
    model = StudentHomework
    fields = ['mark']
    template_name = 'homework_mark.html'
    success_url = '/'


class StudentMarkList(ListView):
    model = Course
    template_name = 'student_mark.html'