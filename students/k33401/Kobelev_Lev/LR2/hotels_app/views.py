from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Room, Booking, Hotel, Review, User
from .forms import ReviewForm, BookingForm
from datetime import datetime, timedelta


class HotelListView(ListView):
    model = Hotel


class HotelDetailView(DetailView):
    model = Hotel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = Room.objects.filter(hotel=self.object.id)
        room_ids = [room["id"] for room in context["rooms"].values()]
        delta = timedelta(days=30)
        context["bookings"] = Booking.objects.filter(reservation__in=room_ids, date_end__gte=(datetime.today()-delta))
        context["reservees"] = User.objects.filter(id__in=set(
            [booking["reservee_id"] for booking in context["bookings"].values()]))
        return context


class RoomDetailView(DetailView):
    model = Room

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        bookings = Booking.objects.filter(reservation=self.object.id)
        booking_ids = [booking['id'] for booking in bookings.values()]
        reviews = Review.objects.filter(booking__in=booking_ids)

        reviews_by_user = 0
        for review in reviews:
            if review.booking.reservee == user:
                reviews_by_user += 1

        for booking in bookings:
            if booking.reservee == user:
                reviews_by_user -= 1

        review_form = ReviewForm()
        if reviews_by_user == 0:
            review_form = None
        booking_form = BookingForm()

        context["reviews"] = reviews
        context["review_form"] = review_form
        context["booking_form"] = booking_form

        return context

    def post(self, request, *args, **kwargs):
        user = request.user
        room = self.get_object()
        if 'review_post' in self.request.POST:
            review_form = ReviewForm(self.request.POST)
            if review_form.is_valid():
                review_form = review_form.save(commit=False)
                review_form.booking = Booking.objects.filter(reservation=room.id, reservee=user).last()
                review_form.save()
        elif 'booking_post' in self.request.POST:
            booking_form = BookingForm(self.request.POST)
            if booking_form.is_valid():
                booking_form = booking_form.save(commit=False)
                booking_form.reservee = user
                booking_form.reservation = room
                booking_form.save()
                return HttpResponseRedirect(reverse('bookings'))
        return HttpResponseRedirect(reverse('get_room',
                                            args=(self.kwargs['hotel_id'], room.id,)))


class BookingListView(ListView):
    model = Booking

    def get_queryset(self):
        return self.model.objects.filter(reservee=self.request.user)


class BookingDeleteView(DeleteView):
    model = Booking
    success_url = '/bookings/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["valid_user"] = True if self.object.reservee == user else False

        return context


class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['date_start', 'date_end']
    success_url = '/bookings/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["valid_user"] = True if self.object.reservee == user else False

        return context
