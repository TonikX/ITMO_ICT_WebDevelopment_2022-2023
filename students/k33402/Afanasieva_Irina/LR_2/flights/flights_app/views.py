from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.shortcuts import render

from .models import *
from .forms import *


# create user
class UserCreateView(CreateView):
    model = User
    fields = ['username', 'password', 'last_name', 'first_name', 'passport']
    success_url = '/success'


# view user info
class UserRetrieveView(DetailView):
    model = User


# create reservation
class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    success_url = '/success'


# view reservation
class ReservationRetrieveView(DetailView):
    model = Reservation


# update reservation data
class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    success_url = '/success'


# delete reservation
class ReservationDeleteView(DeleteView):
    model = Reservation
    success_url = '/success'


# list passengers on specified flight
class PassengerList(ListView):
    model = Reservation
    template_name = 'passenger_list_view.html'


# write review
class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    success_url = '/success'


# success
def success(request):
    return render(request, 'success.html')
