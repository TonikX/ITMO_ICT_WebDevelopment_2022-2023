from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Flight, Booking


# Представление для списка рейсов (табло)
class FlightListView(ListView):
    template_name = "flights/flight_list.html"
    model = Flight


# Представление с информацией о конкретном рейсе
class FlightDetailView(DetailView):
    template_name = "flights/flight_detail.html"
    model = Flight


# Представление для создания бронирования
class BookingCreateView(LoginRequiredMixin, CreateView):
    template_name = "flights/booking_create.html"
    model = Booking
    fields = ["flight", "seats"]
    success_url = "/booking_list"
    login_url = "/login"

    # Заполнение нужного рейса
    def get_initial(self):
        initial = super().get_initial()
        if "flight" in self.request.GET:
            initial["flight"] = self.request.GET.get("flight")
        return initial

    # Получение пользователя
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Представление для обновления бронирования (написание отзыва)
class BookingUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "flights/booking_update.html"
    model = Booking
    fields = ["review_text", "review_number"]
    success_url = "/booking_list"
    login_url = "/login"

    # Фильтрация только бронирований текущего пользователя
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


# Представление со списком бронирований
class BookingListView(LoginRequiredMixin, ListView):
    template_name = "flights/booking_list.html"
    model = Booking
    login_url = "/login"

    # Фильтрация только бронирований текущего пользователя
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
