from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.views.generic import CreateView


def index(request):
    return render(request, 'index.html')


def mlogin(request):
    return render(request, 'login.html')


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


class LogInView(View):
