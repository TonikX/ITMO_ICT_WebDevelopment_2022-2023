from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import DeleteView, UpdateView

from .forms import *
from .models import *


def flights_list(request):
    flights = Flight.objects.all()
    flights = flights.order_by('departure').reverse()
    return render(request, 'flights/flights_list.html', context={'flights': flights})


@login_required(login_url='login_url')
def flight_details(request, slug):
    flight = Flight.objects.get(slug__iexact=slug)
    rates = Ticket.objects.filter(flight__slug=slug).exclude(rate=None)
    passengers = Ticket.objects.filter(flight__slug=slug).order_by('seat')
    form = BuyTicketForm(request.POST or None)

    if request.method == 'POST':
        form = BuyTicketForm(request.POST)
        ticket = form.save(commit=False)
        ticket.user = request.user
        ticket.flight = flight
        if form.is_valid():
            ticket.save()
            return redirect('profile_url')

    isOrdered = Ticket.objects.filter(user__username=request.user.username, flight__slug=slug)

    return render(request, 'flights/flight_page.html',
                  context={'flight': flight, 'form': form, 'ordered': isOrdered, 'rates': rates,
                           'passengers': passengers})


def registration(request):
    if request.user.is_authenticated:
        return redirect('tours_list_url')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))
                return redirect('login_url')
        return render(request, 'flights/registration.html', context={'form': form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('flights_list_url')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile_url')
            else:
                messages.info(request, 'Username OR password is incorrect')

        return render(request, 'flights/login.html', context={})


def logout_user(request):
    logout(request)
    return redirect('login_url')


@login_required(login_url='login_url')
def profile(request):
    tickets = Ticket.objects.filter(user__username__iexact=request.user)
    tickets = tickets.order_by('flight__departure').reverse()
    return render(request, 'flights/profile.html',
                  context={'tickets': tickets})


def ticket_delete(request, pk):
    ticket = Ticket.objects.get(id=pk)
    ticket.delete()
    return redirect('profile_url')


class TicketUpdate(UpdateView):
    model = Ticket
    fields = ['passenger_name', 'passenger_surname', 'passenger_passport']
    success_url = '/profile'
    template_name = 'flights/ticket_update.html'


class ReviewUpdate(UpdateView):
    model = Ticket
    fields = ['rate', 'review_text']
    success_url = '/profile'
    template_name = 'flights/review_update.html'
