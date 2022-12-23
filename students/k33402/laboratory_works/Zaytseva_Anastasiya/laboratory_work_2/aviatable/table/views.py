from table.models import Passenger, Flight, Ticket, Review
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from .forms import NewUserForm
import random
import string

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'auth.html')

def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'auth.html', {'error':'Неверный логин или пароль'})

def logout_view(request):
    logout(request)
    return redirect('/')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    form = NewUserForm()
    return render(request=request, template_name="signup.html", context={"register_form": form})

def tickets(request):
    tickets = Ticket.objects.filter(passenger=request.user.id)
    return render(request, 'tickets.html', {'tickets':tickets})

def order(request, flight_id):
    if request.method == "POST":
        fl = Flight.objects.get(flight_number=request.POST['flight'])
        try:
            tick = Ticket.objects.get(flight=fl.id,seat=request.POST['seat'])
        except Ticket.DoesNotExist:
            ticket = Ticket(
                passenger=Passenger.objects.get(username=request.user.username),
                flight=fl,
                seat=request.POST['seat'],
                ticket_number=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)),
            )
            ticket.save()
            return redirect('/ticket')
        return render(request, 'order.html', {'error': 'Выбранное место занято', 'flight': fl})

    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")

    return render(request, 'order.html', {'flight': flight})


def review(request, flight_number):
    if request.method == "POST":
        fl = Flight.objects.get(flight_number=request.POST['flight'])
        try:
            rev = Review.objects.get(flight=fl.id,passenger=request.user.id)
        except Review.DoesNotExist:
            revNew = Review(
                passenger=Passenger.objects.get(username=request.user.username),
                flight=fl,
                text=request.POST['text'],
                rating=request.POST['rating'],
            )
            revNew.save()
            return redirect('/ticket')
        return render(request, 'review.html', {'error': 'Вы уже оставляли отзыв на данный рейс.', 'flight': fl})

    try:
        flight = Flight.objects.get(flight_number=flight_number)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")

    try:
        rev = Review.objects.get(flight=flight.id,passenger=request.user.id)
    except Review.DoesNotExist:
        return render(request, 'review.html', {'flight': flight})

    return render(request, 'review.html', {'error': 'Вы уже оставляли отзыв на данный рейс.', 'flight': flight})

def reviews(request, flight_number):
    flight = Flight.objects.get(flight_number=flight_number)
    reviews = Review.objects.filter(flight=flight.id)
    return render(request, 'reviews.html', {'reviews': reviews, 'flight': flight})

def passengers(request, flight_number):
    if request.user.username != 'admin':
        raise Http403("Ошибка доступа")

    flight = Flight.objects.get(flight_number=flight_number)
    tickets = Ticket.objects.filter(flight=flight.id)
    passengers = Passenger.objects.filter(id__in=[t.passenger.id for t in tickets])
    return render(request, 'passengers.html', {'passengers': passengers, 'flight': flight})

class FlightList(ListView):
    model = Flight
    template_name = 'table.html'

class TicketDelete(DeleteView):
   model = Ticket
   template_name = 'ticket_delete.html'
   success_url = '/ticket'

class TicketUpdate(UpdateView):
    model = Ticket
    fields = ['seat']
    success_url = '/ticket'
    template_name = 'ticket_update.html'
