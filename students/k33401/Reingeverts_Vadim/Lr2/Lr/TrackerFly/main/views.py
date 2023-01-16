from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect

from .models import Ticket


class TicketList(ListView):
    model = Ticket
    template_name = 'ticket_list.html'
