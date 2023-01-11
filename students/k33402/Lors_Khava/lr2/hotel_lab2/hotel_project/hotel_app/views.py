from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views.generic import ListView, UpdateView, DeleteView
from .forms import ClientForm, BookingForm, CommentForm
from .models import Client, Hotel, Room, Booking, Comment
import datetime

# основная страница
def home(request):
    return render(request, "home.html")

# данные о клиентах
def clients_list(request):
    data = {"clients": Client.objects.all()}
    return render(request, "clients_list.html", data)

# создание нового клиента для регистрации
def clients_create(request):
    data = {}
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/client_list')
    data["form"] = form
    return render(request, "register.html", data)

# данные о номерах
def room_list(request):
    data = {"rooms": Room.objects.all()}
    return render(request, "room_list.html", data)

# бронирование
def book(request):
    data = {}
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
    data["form"] = form
    return render(request, "booking.html", data)

# данные о бронировании
def book_list(request):
    data = {"booking": Booking.objects.all()}
    return render(request, "book_list.html", data)

# cписок клиентов последнего месяца
def last_month(request):
    data = {}
    try:
        month = datetime.date.today() - datetime.timedelta(days=31)
        data["booking"] = Booking.objects.all().filter(check_in_date__gte=str(month),
                                                            check_out_date__lte=str(datetime.date.today()))
        print(data)
    except Booking.DoesNotExist:
        raise Http404("No guests this month yet :(")
    return render(request, "book_list.html", data)

# редактирование брони
class BookUpdate(UpdateView):
    model = Booking
    template_name = "book_update.html"
    fields = ["check_in_date", "check_out_date", "client", "room"]
    success_url = "/book_list/"

# удаление брони
class BookDelete(DeleteView):
    model = Booking
    template_name = "book_delete.html"
    success_url = "/book_list/"

# таблица гостей отеля
class HotelList(ListView):
    model = Hotel
    template_name = 'hotel.html'
    all_hotels = Hotel.objects

# обзор на отели
def hotel_view(request, pk):
    hotel = Hotel.objects.get(id=pk)
    comments = Comment.objects.filter(hotel=hotel)
    return render(request, 'hotel_detail.html', {'hotel': hotel, 'comments': comments})

# написание комментария и просмотр 
def comment(request, pk):
    obj = get_object_or_404(Hotel, id=pk)
    author = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form['review_comment'].value():
            if form['rating'].value():
                if form.is_valid():
                    com = form.save(commit=False)
                    com.client = author
                    com.hotel = obj
                    com.save()
    else:
        form = CommentForm()
    return render(request, 'review.html', {'form': form})
