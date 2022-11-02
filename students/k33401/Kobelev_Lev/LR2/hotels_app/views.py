from django.shortcuts import render, redirect
from django.http import Http404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Room, Booking, Hotel, Review, User
from .forms import ReviewForm, BookingForm


class HotelListView(ListView):
    model = Hotel


class HotelDetailView(DetailView):
    model = Hotel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = Room.objects.filter(hotel=self.object.id)
        room_ids = [room["id"] for room in context["rooms"].values()]
        context["bookings"] = Booking.objects.filter(reservation__in=room_ids)
        context["reservees"] = User.objects.filter(id__in=set(
            [booking["reservee_id"] for booking in Booking.objects.filter(reservation__in=room_ids).values()]))
        return context


def get_room(request, hotel_id, room_number):
    user = request.user

    room_id = Room.objects.filter(hotel=hotel_id, number=room_number).values().first()["id"]
    bookings = Booking.objects.filter(reservation=room_id)
    booking_ids = [booking['id'] for booking in bookings.values()]
    reviews = Review.objects.filter(booking__in=booking_ids)
    rooms = Room.objects.filter(hotel=hotel_id, number=room_number)

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

    if request.method == "POST":
        if 'review_post' in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review_form = review_form.save(commit=False)
                review_form.booking = Booking.objects.filter(reservation=room_id, reservee=user).last()
                review_form.save()
                return redirect(get_room, hotel_id, room_number)
        elif 'booking_post' in request.POST:
            booking_form = BookingForm(request.POST)
            if booking_form.is_valid():
                booking_form = booking_form.save(commit=False)
                booking_form.reservee = user
                booking_form.reservation = rooms[0]
                booking_form.save()
                return redirect(get_room, hotel_id, room_number)

    return render(request, "hotels_app/room_detail.html",
                  context={"room": rooms, "reviews": reviews, "review_form": review_form, "booking_form": booking_form})


class BookingListView(ListView):
    model = Booking

    def get_queryset(self):
        return self.model.objects.filter(reservee=self.request.user)


class BookingDeleteView(DeleteView):
    model = Booking
    success_url = '/bookings/'


class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['date_start', 'date_end']
    success_url = '/bookings/'
