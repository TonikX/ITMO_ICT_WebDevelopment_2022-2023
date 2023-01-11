from django.shortcuts import render, redirect
from .models import Passenger, Flight, Ticket, Comment
from .forms import RegisterForm, CreateBooking, CreateComment
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView


def main_page(request):
    return render(request, 'main.html')


def user_registration(request):
    data = {}
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
    data["form"] = form
    return render(request, 'registration.html', data)


class FlightList(ListView):
    model = Flight
    template_name = 'flight_list.html'


def create_booking(request):
    data = {}
    form = CreateBooking(request.POST or None)
    if form.is_valid():
        form.save()
    data["form"] = form
    return render(request, 'create_booking.html', data)


def my_bookings(request):
    if "passport" in request.POST:
        passport = int(request.POST["passport"])
        return redirect(f'/passenger_bookings/{passport}/')
    else:
        return render(request, 'my_bookings.html')


def passenger_bookings(request, passport):
    passenger = Passenger.objects.get(passport=passport)
    tickets = Ticket.objects.filter(passport=passenger.id)
    return render(request, 'passenger_bookings.html', {'tickets': tickets, 'passenger': passenger})


class TicketUpdate(UpdateView):
    model = Ticket
    fields = ['seat']
    success_url = '/bookings'
    template_name = 'ticket_update.html'


class TicketDelete(DeleteView):
    model = Ticket
    success_url = '/bookings'
    template_name = 'ticket_delete.html'


def all_passengers(request, flight_number):
    flight = Flight.objects.get(flight_number=flight_number)
    tickets = Ticket.objects.filter(flight_number=flight.id)
    passengers = Passenger.objects.filter(id__in=[ticket.passport.id for ticket in tickets])

    return render(request, 'all_passengers.html', {'passengers': passengers, 'flight': flight})


def all_comments(request):
    return render(request, 'all_comments.html', {'object_list': Comment.objects.all()})


def create_comment(request):
    data = {}
    form = CreateComment(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'create_comment.html', data)
