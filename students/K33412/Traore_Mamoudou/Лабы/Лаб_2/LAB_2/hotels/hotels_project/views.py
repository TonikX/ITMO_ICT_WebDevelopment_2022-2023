from datetime import datetime, timedelta

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth import authenticate, login

from .forms import *
from .models import *

from django.contrib.auth import get_user_model
User = get_user_model()


def index(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = EditProfileForm(instance=user)

    context = {
        'form': form
    }
    return render(request, 'edit_profile.html', context)


class ListHotels(ListView):

    model = Hotel
    template_name = 'hotels.html'
    context_object_name = 'hotels'


class ListRooms(ListView):

    template_name = 'rooms.html'
    context_object_name = 'rooms'

    def get_queryset(self):
        return Room.objects.all().order_by('price')


class ListHotelRooms(ListView):

    template_name = 'rooms_by_hotel.html'
    context_object_name = 'hotel'

    def get_queryset(self):
        self.hotel = get_object_or_404(Hotel, pk=self.kwargs['pk'])
        return Room.objects.filter(hotel=self.hotel)


class RoomDetail(DetailView):

    model = Room
    template_name = 'room.html'
    context_object_name = 'room'


class CreateBooking(CreateView):

    form_class = CreateBookingForm
    model = Booking
    template_name = 'create_booking.html'
    context_object_name = 'booking'
    success_url = '/profile/bookings'

    def get_initial(self):
        initial = super(CreateBooking, self).get_initial()
        initial = initial.copy()
        initial['user'] = self.request.user.pk
        initial['room'] = get_object_or_404(Room, pk=self.kwargs['pk'])
        return initial


class ListBookings(ListView):
    template_name = 'bookings_list.html'
    context_object_name = 'bookings_list'

    def get_queryset(self):
        self.user = self.request.user.pk
        return Booking.objects.filter(user=self.user)


class DeleteBooking(DeleteView):

    model = Booking
    template_name = 'delete_booking.html'
    context_object_name = 'booking'
    success_url = '/profile/bookings'


class ListReviews(ListView):

    model = Review
    template_name = 'reviews.html'
    context_object_name = 'reviews'


class CreateReview(CreateView):

    model = Review
    form_class = CreateReviewForm
    template_name = 'create_review.html'
    context_object_name = 'review'
    success_url = '/reviews'

    def get_initial(self):
        initial = super(CreateReview, self).get_initial()
        initial = initial.copy()
        room = Room.objects.get(pk=self.kwargs['pk'])
        room_hotel = getattr(room, 'hotel')

        initial['user'] = self.request.user.pk
        initial['hotel'] = room_hotel
        initial['room'] = room

        return initial


class ListGuests(ListView):

    template_name = 'last_month_guests.html'
    context_object_name = 'guests_list'

    def get_queryset(self):
        last_month = datetime.today() - timedelta(days=30)
        booking_queries = Booking.objects.filter(checked_in=True).filter(date_in__gte=last_month)

        return booking_queries