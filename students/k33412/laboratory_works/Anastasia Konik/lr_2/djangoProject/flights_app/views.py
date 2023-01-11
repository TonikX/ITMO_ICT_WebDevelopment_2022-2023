import time
from flights_app.forms import *
from flights_app.models import User, Flight, Ticket, Feedback
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'auth.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def auth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'auth.html', {'error': 'Try again'})


def registration(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = NewUserForm()
    return render(request, "register.html", {"register_form": form})


def tickets(request):
    user_tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'tickets.html', {'tickets': user_tickets})


def flights(request):
    return render(request, 'flights.html', {'flights': Flight.objects.all()})


def users_list(request, flight_id):
    user_ids = Ticket.objects.filter(flight_id=flight_id).values('user_id')
    users = User.objects.filter(id__in=user_ids)
    flight = Flight.objects.get(id=flight_id)
    return render(request, "users.html", {
        "users": users,
        "flight": flight,
    })


def feedbacks(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    feedbacks = Feedback.objects.filter(flight_id=flight_id)
    return render(request, "feedbacks.html", {
        "feedbacks": feedbacks,
        "flight": flight,
    })


def create_feedback(request, flight_id):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            Feedback.objects.create(comment=form.cleaned_data.get('comment'),
                                    rate=form.cleaned_data.get('rating'),
                                    date=form.cleaned_data.get('date'),
                                    user_id=request.user.id,
                                    flight_id=flight_id)

            return redirect('/flights')
    else:
        form = FeedbackForm()
    return render(request, 'leave_feedback.html', {'form': form})


def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    if ticket.user_id == request.user.id:
        ticket.delete()
    return redirect('/tickets')


def update_ticket(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    if ticket.user_id != request.user.id:
        return redirect('/')
    if request.method == 'POST':
        form = TicketUpdateForm(request.POST)
        if form.is_valid():
            ticket.seat = form.cleaned_data.get('seat')
            ticket.save()
            return redirect('/tickets')
    else:
        form = TicketUpdateForm()
    return render(request, 'update.html', {'form': form, 'ticket': ticket})


def book_flight(request, flight_id):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Ticket.objects.create(flight_id=flight_id,
                                  type=form.cleaned_data.get('type'),
                                  seat=form.cleaned_data.get('seat'),
                                  user_id=request.user.id,
                                  ticket_id=int(str(time.time_ns())[-7:]))
            return redirect('/tickets')
    else:
        form = BookForm()
    return render(request, 'book.html', {'form': form})
