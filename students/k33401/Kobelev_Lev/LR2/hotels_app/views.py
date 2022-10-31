from django.shortcuts import render, redirect
from django.http import Http404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Room, Booking, Hotel, Review
from .forms import ReviewForm, BookingForm


class HotelListView(ListView):
    model = Hotel


def get_hotel_rooms(request, hotel_id):
    context = {"data": Room.objects.filter(hotel=hotel_id)}
    return render(request, "hotels_app/rooms.html", context)


def get_room(request, hotel_id, room_number):
    room_id = Room.objects.filter(hotel=hotel_id, number=room_number).values().first()["id"]
    booking_ids = [booking['id'] for booking in Booking.objects.filter(reservation=room_id).values()]
    reviews = Review.objects.filter(booking__in=booking_ids)
    rooms = Room.objects.filter(hotel=hotel_id, number=room_number)

    review_form = ReviewForm()
    booking_form = BookingForm()

    if request.method == "POST":
        user = request.user
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


def get_bookings(request):
    user = request.user
    context = {"bookings": Booking.objects.filter(reservee=user)}

    return render(request, "hotels_app/booking_list.html", context)


class BookingDeleteView(DeleteView):
    model = Booking
    success_url = '/bookings/'


class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['date_start', 'date_end']
    success_url = '/bookings/'

