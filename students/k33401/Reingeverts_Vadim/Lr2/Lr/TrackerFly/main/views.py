from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.views.generic import RedirectView


from . import models
from . import forms


class Home(TemplateView):
    template_name = 'home.html'


class SignUp(CreateView):
    model = models.User
    form_class = forms.UserSignUpForm
    template_name = 'sign_up.html'

    def get_success_url(self):
        return reverse("home")


class LogIn(LoginView):
    template_name = 'log_in.html'


class LogOut(RedirectView):
    query_string = True
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super(LogOut, self).get_redirect_url(*args, **kwargs)


class Profile(LoginRequiredMixin, TemplateView):
    model = models.User
    template_name = 'profile.html'

    login_url = 'log_in'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context.update({'user': self.request.user})
        return context
