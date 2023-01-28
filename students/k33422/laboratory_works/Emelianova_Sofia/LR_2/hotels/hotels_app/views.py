from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.paginator import Paginator

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import *


#homepage
class Homepage(TemplateView):
    template_name = 'index.html'


# create user
def register(request):
    if request.user.is_authenticated:
        return redirect('/reservation/')
    else:
        form = UserForm()
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()

                return redirect('login')

        data = {'form': form}
        return render(request, 'register.html', data)


#login
def login_(request):
    if request.user.is_authenticated:
        return redirect('/reservation/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/reservation/')

        data = {}
        return render(request, 'login.html', data)


#logout
def logout_(request):
    logout(request)
    return redirect('login')

#hotel detail
def HotelRetriveView(request, pk):
    c = Hotel.objects.get(id=pk)
    reviews = Review.objects.filter(hotel=c)
    return render(request, 'hotel_detail.html', {'hotel': c, 'reviews': reviews})


#reservation list
class ListReservation(ListView):
    model = Reservation
    template_name = 'reservation.html'
    all_reservations = Reservation.objects
    paginate_by = 2

    def get_queryset(self):
        return Reservation.objects.all()


# create reservation
def reservation_create(request, pk):
    obj = get_object_or_404(Hotel, id=pk)
    guest = request.user
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form['hotel'].value():
            res = form.save(commit=False)
            res.guest = guest
            res.hotel = obj
            res.save()
            return redirect('/reservation')
    else:
        form = ReservationForm()
    return render(request, 'reservation_create.html', {'form': form})
#class ReservationCreateView(CreateView):
#    model = Reservation
#    form_class = ReservationForm
#    template_name = 'reservation_create.html'


# view reservation
class ReservationRetrieveView(DetailView):
    model = Reservation
    template_name = 'reservation_detail.html'


# update reservation data
class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_update.html'


# delete reservation
class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'reservation_delete.html'


# hotels list
class HotelList(ListView):
    model = Hotel
    template_name = 'hotel.html'
    all_hotels = Hotel.objects
    paginate_by = 3


# write review
def add_comment(request, pk):
    obj = get_object_or_404(Hotel, id=pk)
    author = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form['comment'].value():
            if form['rating'].value():
                if form.is_valid():
                    com = form.save(commit=False)
                    com.author = author
                    com.hotel = obj
                    com.save()
                    return redirect('/hotel')
            else:
                messages.info(request, 'Вы должны поставить оценку')
        else:
            messages.info(request, 'Вы должны оставить коментарий')
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form})


#guests list
class GuestsList(ListView):
    model = Reservation
    template_name = 'guests.html'