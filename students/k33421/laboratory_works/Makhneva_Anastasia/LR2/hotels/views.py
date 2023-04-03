from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, FormView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Hotel, RoomType, Room, Reservation, Comment
from .forms import CommentForm, ReservationForm


class CustomLoginView(LoginView):
    template_name = 'hotels/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('hotels')


class RegisterPage(FormView):
    template_name = 'hotels/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('hotels')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('hotels')
        return super(RegisterPage, self).get(*args, **kwargs)


class HotelsList(ListView):
    model = Hotel
    template_name = 'hotels/hotels_list.html'
    context_object_name = 'hotels'


def hotel_detail(request, hotel_id):
    hotel = Hotel.objects.get(pk=hotel_id)
    rooms = Room.objects.filter(hotel__pk=hotel_id)
    context = {'hotel': hotel, 'rooms': rooms}
    return render(request, 'hotels/hotel_detail.html', context)


def room_detail(request, hotel_id, room_id):
    hotel = Hotel.objects.get(pk=hotel_id)
    room = Room.objects.get(pk=room_id)
    if request.user.is_authenticated:
        reservations = Reservation.objects.filter(
            room__id=room_id, guest=request.user)
    else:
        reservations = None
    comments = Comment.objects.filter(reservation__room__id=room_id)
    initial = {'reservation': reservations}
    comment_form = CommentForm(initial=initial)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            c_form. save()
        else:
            comment_form = c_form
    context = {'hotel': hotel, 'room': room,
               'comment_form': comment_form, 'comments': comments}
    return render(request, 'hotels/room.html', context)


@login_required
def reservation_view(request, hotel_id, room_id,):
    room = Room.objects.get(pk=room_id)
    initial = {'room': room, 'guest': request.user}
    form = ReservationForm(initial=initial)
    if request.method == 'POST':
        c_form = ReservationForm(request.POST)
        if c_form.is_valid():
            c_form. save()
            return redirect(f'/hotel/{hotel_id}/room/{room_id}')
        else:
            form = c_form
    context = {'room': room, 'form': form}
    return render(request, 'hotels/reservation.html', context)


class ReservationList(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'hotels/reservations.html'
    context_object_name = 'reservations'


class DeleteReservationView(LoginRequiredMixin, DeleteView):
    model = Reservation
    context_object_name = 'reservation'
    success_url = reverse_lazy('reservations')
