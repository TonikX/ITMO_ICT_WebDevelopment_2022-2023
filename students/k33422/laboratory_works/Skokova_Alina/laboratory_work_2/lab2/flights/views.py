from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.views.generic import CreateView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from django.contrib import messages


class UserRegister(CreateView):
    form_class = UserRegisterForm
    success_url = "/login"
    template_name = 'flights/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'flights/login.html'

    def get_success_url(self):
        return "/"


def logout_user(request):
    logout(request)
    return redirect('/login')


class FlightsList(ListView):
    template_name = 'flights/list_flights.html'
    queryset = Flight.objects.all()
    paginate_by = 10


@login_required
def book_flight(request, id_flight):
    c = Flight.objects.get(pk=id_flight)
    context = {}

    form = BookingForm(request.POST or None)
    if form.is_valid():
        response = form.save(commit=False)
        response.passport = request.user
        response.id_flight = c
        form.save()
        messages.success(request, f'Место зарезервировано!')
    context['form'] = form
    context['flight'] = c
    return render(request, "flights/book_flight.html", context)

class BookingsList(ListView):
    model = Booking
    template_name = 'flights/my_bookings.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(BookingsList, self).get_queryset()
        queryset = queryset.filter(passport=self.request.user)
        return queryset


class BookingUpdate(UpdateView):
    model = Booking
    fields = ['luggage']
    success_url = '/my_bookings/'


class BookingDelete(DeleteView):
    model = Booking
    success_url = '/my_bookings/'


class PassengersList(ListView):
    model = Booking
    template_name = 'flights/all_passengers.html'
    paginate_by = 10

    def get_queryset(self):
        return Booking.objects.filter(id_flight=self.kwargs['id_flight'], approved="Y")


class ReviewsList(ListView):
    template_name = 'flights/list_reviews.html'
    queryset = Review.objects.all()
    paginate_by = 10


@login_required
def review_create(request):
    context = {}

    form = ReviewForm(request.POST or None)
    if form.is_valid():
        response = form.save(commit=False)
        response.author = request.user
        form.save()
        messages.success(request, f'Отзыв добавлен!')
    context['form'] = form
    return render(request, "flights/review_create.html", context)