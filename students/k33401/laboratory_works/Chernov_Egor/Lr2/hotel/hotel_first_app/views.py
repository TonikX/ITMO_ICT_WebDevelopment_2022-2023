from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import *
from django.views.generic import CreateView


def index(request):
    return render(request, 'index.html')


def mlogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...
    # return render(request, 'login.html')


def mlogout(request):
    return redirect('/')


def home(request):
    return render(request, 'home.html')


class RegView(CreateView):
    form_class = CustomUserCreationForm
    success_url = 'home/'
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        super(RegView, self).post(request)
        login_username = request.POST['username']
        login_password = request.POST['password1']
        user = authenticate(username=login_username, password=login_password)
        login(request, user)
        return redirect(self.success_url)


class LogInView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class LogOutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('index')
