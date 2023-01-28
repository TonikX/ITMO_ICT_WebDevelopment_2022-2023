from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Tour, Reservation, Review


# Список доступных туров
class TourListView(LoginRequiredMixin, ListView):
    model = Tour
    template_name = "tours/tours.html"
    queryset = Tour.objects.order_by("destination")  # Туры сортируются по пункту назначения
    login_url = reverse_lazy("login")

    # Показывает только те туры где есть место
    def get_queryset(self):
        queryset = self.queryset
        ids = [tour.id for tour in queryset if tour.empty_count > 0]
        return queryset.filter(pk__in=ids)


# Список резервирований пользователя
class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = "tours/reservations.html"
    queryset = Reservation.objects.none()  # Задаем queryset чтобы django не выдавал ошибку
    login_url = reverse_lazy("login")

    # Выбирает только резервирования текущего пользователя
    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)


# Информация о туре + отзывы
class TourAndReviewsView(LoginRequiredMixin, DetailView):
    model = Tour
    template_name = "tours/reviews.html"
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        # Fetch comments for room
        context = super(TourAndReviewsView, self).get_context_data(**kwargs)
        review_ids = []
        for reservation in self.get_object().reservations.all():
            if reservation.has_review:
                review_ids.append(reservation.review.pk)
        context['reviews'] = Review.objects.filter(pk__in=review_ids)
        return context


# Создание резервирования
class CreateReservationView(LoginRequiredMixin, CreateView):
    model = Reservation
    template_name = "tours/reserve.html"
    fields = ("tour", "count")
    success_url = reverse_lazy("reservations")
    login_url = reverse_lazy("login")

    # Добавляет текущего пользователя в модель
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateReservationView, self).form_valid(form)

    # Выбирает нужный тур в поле если он уже указан в ссылке
    def get_initial(self):
        initial = super(CreateReservationView, self).get_initial()
        if 'select' in self.request.GET:
            initial['tour'] = self.request.GET.get('select')
        return initial


# Создание отзыва
class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = "tours/write.html"
    fields = ("text", "stars")
    success_url = reverse_lazy("reservations")
    login_url = reverse_lazy("login")

    # Привязывает комментарий к резервированию по url
    def form_valid(self, form):
        form.instance.reservation = get_object_or_404(Reservation, pk=int(self.request.GET['reservation']))
        return super(CreateReviewView, self).form_valid(form)
