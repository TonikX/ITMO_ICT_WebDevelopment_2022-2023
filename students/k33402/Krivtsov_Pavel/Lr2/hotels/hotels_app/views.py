from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView

from .models import Hotel, Room


class HotelList(ListView):
    model = Hotel
    template_name = "hotel_list.html"


def hotel_info(request, pk):
    hotel = get_object_or_404(Hotel, id=pk)
    rooms = Room.objects.filter(hotel=hotel)
    context = {"hotel": hotel, "rooms": rooms}

    return render(request, "hotel_info.html", context)
