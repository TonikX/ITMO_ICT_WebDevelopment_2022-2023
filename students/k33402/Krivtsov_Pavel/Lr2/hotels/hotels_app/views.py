from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from datetime import datetime
import pytz

from .models import Hotel, Room, Reservation
from .forms import RegisterUserForm, ReserveForm


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация"

        return context


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Авторизация"

        return context

    def get_success_url(self):
        next_page = self.request.GET.get("next", default="/")
        return next_page


def logout_user(request):
    logout(request)
    return redirect('hotels')


class HotelList(ListView):
    model = Hotel
    template_name = "hotel_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Hotels"

        return context


class HotelInfo(DetailView):
    model = Hotel
    template_name = "hotel_info.html"
    context_object_name = "hotel"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['hotel'].name
        context['rooms'] = Room.objects.filter(hotel=context['hotel'])

        return context


class RoomInfo(DetailView):
    model = Room
    template_name = "room_info.html"
    context_object_name = "room"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['room'].name

        return context


def reserve_room(request, pk):
    def is_dates_valid(date_start, date_end) -> bool:
        return date_start < date_end

    def is_dates_free(date_start, date_end, room_id) -> bool:
        reservations = Reservation.objects.filter(room=room_id)
        for old_reservation in reservations:
            if old_reservation.date_start < date_end or old_reservation.date_end > date_start:
                return False

        return True

    room = get_object_or_404(Room, id=pk)
    form = ReserveForm(request.POST or None)
    if form.is_valid():
        date_start = datetime.strptime(request.POST['date_start'], '%Y-%m-%d').replace(tzinfo=pytz.UTC)
        date_end = datetime.strptime(request.POST['date_end'], '%Y-%m-%d').replace(tzinfo=pytz.UTC)

        if not is_dates_valid(date_start, date_end):
            messages.error(request, 'Дата выезда должна быть после даты заезда. Попробуйте заново')
            return redirect(f'reserve', pk=pk)

        if not is_dates_free(date_start, date_end, pk):
            messages.error(request, 'Выбранные даты заняты. Попробуйте другие')
            return redirect(f'reserve', pk=pk)

        form = form.save(commit=False)
        form.user = request.user
        form.room = room
        form.save()

    return render(request, "reserve.html", {"title": "Резервирование" + " " + room.name, "form": form})
