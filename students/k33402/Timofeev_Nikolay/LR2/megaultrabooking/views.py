from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

from .forms import UserForm, HotelForm, RoomForm, ReviewForm, BookingForm, EditBookingForm
from .models import BookingState, Hotel, Room, Review, Booking


# XXX: Регистрация новых пользователей.
# XXX: Просмотр и резервирование номеров. Пользователь должен иметь возможность редактирования и удаления своих резервирований.
# XXX: Написание отзывов к номерам. При добавлении комментариев, должны сохраняться период проживания, текст комментария, рейтинг (1-10), информация о комментаторе.
# XXX: Администратор должен иметь возможность заселить пользователя в отель и выселить из отеля средствами Django-admin. 
# В клиентской части должна формироваться таблица, отображающая постояльцев отеля за последний месяц.



def hotels_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels_list.html', {'hotels': hotels})

def rooms_list(request, hotel_id):
    rooms = Room.objects.filter(hotel_id=hotel_id)
    hotel = Hotel.objects.filter(id=hotel_id).first()
    return render(request, 'rooms_list.html', {'rooms': rooms, "hotel": hotel})

def reviews_list(request, hotel_id, room_id):
    room = Room.objects.filter(pk=room_id).first()
    reviews = Review.objects.filter(booking__room=room_id)
    return render(request, 'reviews_list.html', {'reviews': reviews, 'room': room})

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('/hotels/')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


@login_required
def add_hotel(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hotels/')
    else:
        form = HotelForm()

    return render(request, 'add_hotel.html', {'form': form})

@login_required
def add_room(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id, owner=request.user)

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.hotel = hotel
            room.save()
            return redirect('rooms_list', hotel_id=hotel_id)
    else:
        form = RoomForm()

    return render(request, 'add_room.html', {'hotel_id': hotel_id, 'form': form})

@login_required
def add_review(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.booking = booking
            review.ts_created = date.today().isoformat()
            review.save()
            return redirect('/hotels/')
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form, 'booking': booking})

@login_required
def bookings_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings_list.html', {'bookings': bookings})


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    if request.method == 'POST':
        form = EditBookingForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['cancel'] and booking.state == BookingState.PENDING:
                booking.state = BookingState.CANCELED
            if new_start := form.cleaned_data['ts_start']:
                booking.ts_start = new_start
            if new_end := form.cleaned_data['ts_end']:
                booking.ts_end = new_end
            booking.save()
            return redirect('personal')
    else:
        form = EditBookingForm()

    return render(request, 'edit_booking.html', {'form': form, 'booking': booking})



@login_required
def add_booking(request, hotel_id, room_id):
    room = get_object_or_404(Room, pk=room_id, hotel__id=hotel_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.user = request.user
            booking.save()
            return redirect('personal')
    else:
        form = BookingForm()

    return render(request, 'add_booking.html', {'form': form, 'room': room})


@login_required
def personal_page(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'personal.html', {'bookings': bookings})

def hotel_statistics(request, hotel_id):
    hotel = Hotel.objects.get(pk=hotel_id)
    booking_statistics = hotel.get_last_month_booking_statistics()
    visitors = hotel.get_last_month_visitors()

    return render(request, 'hotel_stats.html', {
        'booking_statistics': booking_statistics,
        'visitors': visitors,
        'hotel': hotel
    })

