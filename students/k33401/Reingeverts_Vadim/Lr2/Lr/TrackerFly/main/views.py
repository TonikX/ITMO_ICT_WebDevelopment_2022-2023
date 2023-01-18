from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect

from . import models


class Home(TemplateView):
    template_name = 'home.html'


class SignUp(TemplateView):
    template_name = 'sign_up.html'


class LogIn(TemplateView):
    template_name = 'log_in.html'
