from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm, CustomAuthenticationForm


class RegView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'index.html'
    success_url = 'hotels'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        context = {'username': ""}
        print('before', context['username'])
        if form.is_valid():
            form.save()
            context['username'] = form.cleaned_data.get('username')
            print('inside', context['username'])
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            login(request, user)
            return render(request, 'hotels.html', context)
        print('after', context['username'])
        return render(request, 'hotels.html', context)


class LogInView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('hotels')


class LogOutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('index')
