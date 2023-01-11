from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Guest, Room, Accommodation, Hotel, Comment
from .forms import GuestForm, AccommodationForm, CommentForm
from django.views.generic import UpdateView, DeleteView
from django.views.generic.list import ListView
import datetime


def guest_list(request):
    data = {"guests": Guest.objects.all()}
    return render(request, "guest_list.html", data)


def guest_create(request):
    data = {}
    form = GuestForm(request.POST or None)
    if form.is_valid():
        form.save()
    data["form"] = form
    return render(request, "guest_create.html", data)


def room_list(request):
    data = {"rooms": Room.objects.all()}
    return render(request, "room_list.html", data)


def book(request):
    data = {}
    form = AccommodationForm(request.POST or None)
    if form.is_valid():
        form.save()
    data["form"] = form
    return render(request, "book.html", data)


def book_list(request):
    data = {"accoms": Accommodation.objects.all()}
    return render(request, "accom_list.html", data)


def last_month(request):
    data = {}
    try:
        month = datetime.date.today() - datetime.timedelta(days=31)
        data["accoms"] = Accommodation.objects.all().filter(check_in_date__gte=str(month),
                                                            check_out_date__lte=str(datetime.date.today()))
        print(data)
    except Accommodation.DoesNotExist:
        raise Http404("No guests this month yet :(")
    return render(request, "accom_list.html", data)


def accommodation_list(request):
    data = {"accoms": Accommodation.objects.all()}
    return render(request, "accom_list.html", data)


def home(request):
    return render(request, "home.html")


class AccomUpdate(UpdateView):
    model = Accommodation
    template_name = "accom_update.html"
    fields = ["check_in_date", "check_out_date", "guest", "room"]
    success_url = "/accom/list/"


class AccomDelete(DeleteView):
    model = Accommodation
    template_name = "accom_delete.html"
    success_url = "/accom/list/"


class HotelList(ListView):
    model = Hotel
    template_name = 'hotel.html'
    all_hotels = Hotel.objects


def hotel_view(request, pk):
    hotel = Hotel.objects.get(id=pk)
    comments = Comment.objects.filter(hotel=hotel)
    return render(request, 'hotel_detail.html', {'hotel': hotel, 'comments': comments})


def comment(request, pk):
    obj = get_object_or_404(Hotel, id=pk)
    author = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form['comment'].value():
            if form['rating'].value():
                if form.is_valid():
                    com = form.save(commit=False)
                    com.author = author
                    com.hotel = obj
                    com.save()
    else:
        form = CommentForm()
    return render(request, 'review.html', {'form': form})
