from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render, redirect, reverse

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


class LogIn(FormView):
    model = models.User
    form_class = forms.UserLogInForm
    template_name = 'log_in.html'
    success_url = ""

    fields = ["username", "password"]
