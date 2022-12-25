from django.shortcuts import render, redirect
from django.http import Http404
from hotels.models import Hotel, Booking, Room, Guest, Feedback
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from hotels.forms import CreateFeedback


# главная страница
def main_page(request):
    return render(request, 'main_page.html')


# создание нового пользователя
class AddGuests(CreateView):
    model = Guest
    fields = [
        "last_name",
        "first_name",
        "passport",
    ]
    template_name = "add_guest.html"
    success_url = "/main/"


# просмотр всех номеров
class ListRooms(ListView):
    model = Room
    template_name = 'list_rooms.html'

# создание бронирования
class CreateBooking(CreateView):
    model = Booking
    fields = [
        'hotel',
        'room',
        'guest',
        'date_start',
        'date_end'
    ]
    template_name = 'create_booking.html'
    success_url = '/bookings/my/'

# редактирование бронирования
class UpdateBooking(UpdateView):
    model = Booking
    fields = ['room', 'date_start', 'date_end']
    template_name = 'update_booking.html'
    success_url = '/bookings/my/'


# удаление бронирования
class DeleteBooking(DeleteView):
    model = Booking
    template_name = 'delete_booking.html'
    success_url = '/bookings/my/'


# просмотр бронирований пользователя
def UserBookings(request, guest_passport):
    need_book = Booking.objects.filter(guest=guest_passport)
    current_book = {"object_list": need_book}
    return render(request, 'users_bookings.html', current_book)


# отбор паспорта для просмотра бронирований
def MyBookings(request):
    try:
        passport = int(request.POST.get('passport_user'))
        return redirect(f"/bookings/{passport}/")
    except:
        return render(request, "my_bookings.html")


# написать комментарий
def AddFeedback(request):
    data = {}
    form = CreateFeedback(request.POST)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'give_feedback.html', data)


# посмотреть все комментарии
def AllFeedbacks(request):
    list_comments = {"object_list": Feedback.objects.all()}
    return render(request, 'all_feedbacks.html', list_comments)


# таблица гостей отеля
def get_hotel(request):
    hotel = request.POST.get('hotel_name')
    if hotel:
        return redirect(f"/guests/{hotel}")
    else:
        return render(request, 'hotel.html')


def guests_list(request, hotel_name):
    guest_in_hotel = Booking.objects.filter(hotel=hotel_name).values_list('guest')
    nedeed_guests = Guest.objects.filter(passport__in=guest_in_hotel)
    list_of_guests = {
        "object_list": nedeed_guests,
        "hotel_name": hotel_name}
    return render(request, 'guests.html', list_of_guests)
