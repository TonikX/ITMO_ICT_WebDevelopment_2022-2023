import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import RegisterUserForm, LoginForm, ReviewForm
from .models import *


# Create your views here.

def flights(request):
    flights_list = Flight.objects.all()

    if request.method == "GET":
        return render(request, "avia/index.html", context={"flights": flights_list})


def get_flight(request, slug):
    flight = Flight.objects.get(flight_number__exact=slug)

    if request.method == "GET":
        return render(request, "avia/certain_flight.html", context={"flight": flight})


def book(request):
    flight = Flight.objects.get(flight_number__exact=request.POST['flight_number'])
    next_page = request.POST['next']
    seat = request.POST['seat']
    passenger = User.objects.get(id__exact=request.user.id)
    try:
        ticket = Ticket.objects.get(flight_number__exact=flight, passenger_id__exact=passenger.id)
        ticket.seat = seat
        ticket.save()
    except Ticket.DoesNotExist:
        print("Doesnt exist")
        Ticket.objects.create(ticket_number=random.randint(100000, 999999),
                              flight_number=flight,
                              passenger=passenger,
                              seat=seat
                              )

    return redirect(next_page)


def get_passengers(request, slug):
    tickets = Flight.objects.get(flight_number__exact=slug).ticket_set.get_queryset()

    return render(request, "avia/passengers_list.html", context={"tickets": tickets, "flight_n": slug})


def get_reviews(request):
    reviews = Comment.objects.all()

    return render(request, 'avia/reviews.html', context={'reviews': reviews})


def register(request):
    if request.method == "GET":
        register_form = RegisterUserForm()
        print(register_form)
        return render(request, 'avia/registration.html', context={'form': register_form})

    if request.method == "POST":
        register_form = RegisterUserForm(request.POST)

        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect("flights_url")


def login_req(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'avia/login.html', context={'form': form})

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('flights_url')
            else:
                return render(request, 'avia/login.html', {'form': form,
                                                           'err': 'Incorrect username/password'})
        else:
            return render(request, 'avia/login.html', {'form': form})


def logout_req(request):
    logout(request)
    return redirect('flights_url')


def get_bookings(request):
    tickets = Ticket.objects.filter(passenger_id__exact=request.user.id)

    return render(request, 'avia/bookings.html', context={'tickets': tickets})


def get_certain_book(request, slug):
    ticket = Ticket.objects.get(ticket_number__exact=slug)
    flight = Flight.objects.get(flight_number__exact=ticket.flight_number)
    passenger = User.objects.get(id__exact=request.user.id)

    return render(request, 'avia/get_certain_book.html', context={'ticket': ticket,
                                                                  'flight': flight,
                                                                  'passenger': passenger})


def delete_certain_book(request, slug):
    ticket = Ticket.objects.get(ticket_number__exact=slug)
    ticket.delete()

    return get_bookings(request)


def send_review(request, slug):
    if request.method == "GET":
        form = ReviewForm()
        return render(request, 'avia/review.html', context={'form': form})

    if request.method == "POST":
        form = ReviewForm(request.POST)
        rate = request.POST['rating']
        text = request.POST['text']

        if form.is_valid():
            ticket = Ticket.objects.get(ticket_number__exact=slug)
            flight = ticket.flight_number
            passenger = User.objects.get(id__exact=request.user.id)
            Comment.objects.create(comment_number=random.randint(10000, 99999),
                                   author=passenger,
                                   flight=flight,
                                   rating=rate,
                                   text=text
                                   )

            return redirect('get_reviews_url')

        else:
            return render(request, 'avia/reviews.html', context={'form': form})