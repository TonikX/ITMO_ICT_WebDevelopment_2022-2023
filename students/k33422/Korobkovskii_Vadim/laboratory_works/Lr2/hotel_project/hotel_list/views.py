from django.core.paginator import Paginator
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import *


class Homepage(TemplateView):
    template_name = 'index.html'


def register(request):
    if request.user.is_authenticated:
        return redirect('/main_page/')
    else:
        form = UserForm()
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()

                return redirect('login')

        data = {'form': form}
        return render(request, 'register.html', data)


def login_(request):
    if request.user.is_authenticated:
        return redirect('/main_page/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/main_page/')

        data = {}
        return render(request, 'login.html', data)


def logout_(request):
    logout(request)
    return redirect('login')


class IndexView(TemplateView):
    template_name = "index1.html"


class HotelRetrieveView(DetailView):
    model = Hotel
    template_name = 'hotel_detail.html'


class ListReservation(ListView):
    model = Reservation
    template_name = 'reservation.html'
    all_reservations = Reservation.objects
    paginate_by = 10


class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_create.html'


def create_reservation(request):
    data = {}
    form = ReservationForm(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, "reservation_create.html", data)


class ReservationRetrieveView(DetailView):
    model = Reservation
    template_name = 'reservation_detail.html'


class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_update.html'


class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'reservation_delete.html'


class HotelList(ListView):
    model = Hotel
    template_name = 'hotel.html'
    all_hotels = Hotel.objects
    paginate_by = 10


class GuestsList(ListView):
    model = Reservation
    template_name = 'guests.html'
    all_guests = Reservation.objects
    paginate_by = 10


class ListRoom(ListView):
    model = Room
    template_name = "room_list.html"
    all_rooms = Room.objects
    paginate_by = 10


class RoomRetrieveView(DetailView):
    model = Room
    template_name = "room_detail.html"


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "review_create.html"


class ReviewList(ListView):
    model = Review
    template_name = "review.html"
    all_review = Review.objects
    paginate_by = 10


class ReviewRetrieveView(DetailView):
    model = Review
    template_name = "review_detail.html"

