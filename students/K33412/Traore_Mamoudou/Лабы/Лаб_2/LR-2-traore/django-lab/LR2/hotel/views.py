from django.contrib.auth.views import LoginView
from django.db.models import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView
from .models import *
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login, logout
from .forms import *
from datetime import datetime as dt
import datetime

from .models import Booking


# Основная страница
class HomePageView(TemplateView):
    template_name = 'home.html'


# Перевод на профиль
def profile(request):
    return render(request, 'profile.html')


# Регистрация
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')

    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


# Выйти из профиля (выкинет на главную)
def logout_view(request):
    logout(request)
    return redirect('/')


# Список отелей
class ListHotels(ListView):
    model = Hotel
    template_name = 'hotels.html'
    context_object_name = 'hotels'


# Список номеров в отеле
class ListHotelRooms(ListView):
    template_name = 'hotelrooms.html'
    context_object_name = 'hotel'

    def get_queryset(self):
        self.hotel = get_object_or_404(Hotel, pk=self.kwargs['pk'])
        return Room.objects.filter(hotel=self.hotel)


# Создать бронь
class CreateBooking(CreateView):
    form_class = CreateBookingForm
    model = Booking
    template_name = 'newbooking.html'
    context_object_name = 'booking'
    success_url = '/profile/bookings'

    def get_initial(self):
        initial = super(CreateBooking, self).get_initial()
        initial = initial.copy()
        initial['client'] = self.request.user.pk
        initial['room'] = get_object_or_404(Room, pk=self.kwargs['pk'])
        return initial


# Список бронирований
class ListBookings(ListView):
    model = Booking
    template_name = 'bookings_list.html'
    context_object_name = 'bookings_list'

    def get_queryset(self):
        self.client = self.request.user.pk
        return Booking.objects.filter(client=self.client)


# Удалить бронь
class DeleteBooking(DeleteView):
    model = Booking
    template_name = 'delete_booking.html'
    context_object_name = 'booking'
    success_url = '/profile/bookings'


# Список отзывов
class ListReviews(ListView):
    model = Review
    template_name = 'reviews.html'
    context_object_name = 'reviews'


# Создать отзыв
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


# Список постояльцев последнего месяца
class ListGuests(ListView):
    template_name = 'lastguests.html'
    context_object_name = 'guests_list'

    def get_queryset(self):
        last_month = datetime.date.today() - datetime.timedelta(days=30)
        booking_queries = Booking.objects.filter(check_in=True).filter(start_date__gte=last_month)

        return booking_queries