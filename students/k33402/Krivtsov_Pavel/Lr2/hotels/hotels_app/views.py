from django.contrib import messages
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from datetime import datetime
import pytz
import typing as tp

from .models import Hotel, Room, Reservation, Comment
from .forms import RegisterUserForm, ReserveForm, InputCommentForm


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


def profile(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, "profile.html", {"title": "Профиль", "reservations": reservations})


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


def room_info(request, pk):
    room = get_object_or_404(Room, id=pk)
    comments = Comment.objects.filter(room=room)

    if request.method == "POST":
        form = InputCommentForm(request.user, room, request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.room = room
            form.save()

            return redirect("room_info", pk=pk)
    else:
        if request.user.is_authenticated:
            form = InputCommentForm(request.user, room)
        else:
            form = InputCommentForm(None, None)

    return render(request, "room_info.html", {"title": room.name, "room": room, "comments": comments, "form": form})


class ReservationView:
    @staticmethod
    def _is_dates_valid(date_start, date_end) -> bool:
        return (date_start < date_end) and (date_start > datetime.now(tz=pytz.UTC))

    @staticmethod
    def _is_dates_free(date_start, date_end, room_id, user_id) -> bool:
        reservations = Reservation.objects.filter(room=room_id).exclude(user=user_id)
        for old_reservation in reservations:
            if (old_reservation.date_start < date_start < old_reservation.date_end) or \
                    (old_reservation.date_start < date_end < old_reservation.date_end):
                return False

        return True

    @staticmethod
    def _check_dates(request, room_id, user_id) -> tp.Tuple[bool, str]:
        date_start = datetime.strptime(request.POST['date_start'], '%Y-%m-%d').replace(tzinfo=pytz.UTC)
        date_end = datetime.strptime(request.POST['date_end'], '%Y-%m-%d').replace(tzinfo=pytz.UTC)

        if not ReservationView._is_dates_valid(date_start, date_end):
            return False, 'Дата заезда должна быть позже сегодняшней и раньше даты выезда. Попробуйте заново'

        if not ReservationView._is_dates_free(date_start, date_end, room_id, user_id):
            return False, 'Выбранные даты заняты. Попробуйте другие'

        return True, ''

    @staticmethod
    def reserve_room(request, pk):
        room = get_object_or_404(Room, id=pk)
        form = ReserveForm(request.POST or None)
        if form.is_valid():
            dates_check = ReservationView._check_dates(request, pk, request.user.id)

            if not dates_check[0]:
                messages.error(request, dates_check[1])
                return redirect('reserve', pk=pk)

            form = form.save(commit=False)
            form.user = request.user
            form.room = room
            form.save()
            return redirect('profile')

        return render(request, "reserve.html", {"title": room.name, "form": form})

    @staticmethod
    def update_reservation(request, pk):
        reservation = get_object_or_404(Reservation, id=pk)
        form = ReserveForm(request.POST or None, instance=reservation)

        if not reservation.user == request.user:
            return redirect(f'profile')

        if form.is_valid():
            dates_check = ReservationView._check_dates(request, reservation.room.id, request.user.id)
            if not dates_check[0]:
                messages.error(request, dates_check[1])
                return redirect('update_reservation', pk=pk)

            form.save()
            return redirect('profile')

        return render(request, "update_reservation.html", {"title": "Изменить бронирование", "form": form})

    @staticmethod
    def delete_reservation(request, pk):
        reservation = Reservation.objects.get(id=pk)

        if request.user.id != reservation.user.id:
            return redirect('profile')

        if request.method == 'POST':
            reservation.delete()
            return redirect('profile')

        return render(request, 'delete_reservation.html', {'title': 'Отмена бронирования', 'reservation': reservation})


def guests_info(request):
    reservations = Reservation.objects.filter(date_start__month__lte=datetime.now().month, date_end__month__gte=datetime.now().month)

    hotels_guests: tp.Dict[Hotel, tp.Set[str]] = {}
    for reservation in reservations:
        if reservation.room.hotel in hotels_guests:
            hotels_guests[reservation.room.hotel].add(reservation.user.username)
        else:
            hotels_guests[reservation.room.hotel] = {reservation.user.username}

    return render(request, "guests.html", {"title": "Постояльцы", "hotels_guests": hotels_guests, "month": datetime.now().strftime("%B")})

