from django.shortcuts import render, redirect
from msilib.schema import ListView
from django.http import Http404 
from .models import Hotel, Reservation,Room, Guest, Comment
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .forms import CreateComment, CreateReservation


#для главной страницы
def main_page(request):
    return render(request, 'main_page.html')

#создание нового пользователя
class RegGuests(CreateView):
    model = Guest
    fields = [
        "first_name",
        "last_name",
        "passport",
    ]
    template_name = "register_guests.html"
    success_url = '/registration/'

#просмотр всех номеров
class RoomsList(ListView):
    model = Room
    template_name = 'list_rooms.html'

#бронирование
def create_reservation(request):
    data = {}
    form = CreateReservation(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'create_reservation.html', data)

#просмотр бронирований пользователя
def user_book(request, guest_passport):
    need_book = Reservation.objects.filter(guest =  guest_passport) 
    current_book = {"object_list": need_book}
    return render(request, 'users_bookings.html', current_book)

#отбор паспорта для просмотра бронирований
def my_bookings(request):
    try:
        passport = int(request.POST.get('passport_user'))
        return redirect(f"/users_bookings/{passport}/")
    except:
        return render(request, "my_bookings.html")

#редактирование брони
class UpdateBooking(UpdateView):
    model = Reservation
    fields = ['room', 'arrival_date', 'departure_date']
    template_name = 'update_book.html'
    success_url = '/my_bookings/'

#удаление брони
class DeleteBooking(DeleteView):
    model = Reservation
    template_name = 'del_book.html'
    success_url = '/my_bookings/'

#написать комментарий
def create_comment(request):
    data = {}
    form = CreateComment(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'create_comment.html', data)

#посмотреть все комментарии
def all_comments(request):
    list_comments = {"object_list": Comment.objects.all()}
    return render(request, 'all_comments.html', list_comments)

#таблица гостей отеля
def get_hotel(request):
    hotel = request.POST.get('hotel_name')
    if hotel:
        return redirect(f"/guests/{hotel}")
    else:
        return render(request, 'hotel.html')

def guests_list(request, hotel_name):
    guest_in_hotel = Reservation.objects.filter(hotel = hotel_name).values_list('guest')
    nedeed_guests = Guest.objects.filter(passport__in = guest_in_hotel )
    list_of_guests = {
        "object_list": nedeed_guests,
        "hotel_name" : hotel_name}
    return render(request, 'guests.html', list_of_guests)
