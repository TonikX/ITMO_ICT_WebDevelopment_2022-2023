from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Hotel, Room


class HotelList(ListView):
    model = Hotel
    template_name = "hotel_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Hotels"

        return context


class HotelInfo(DetailView):
    model = Hotel
    template_name = "hotel_info.html"
    context_object_name = "hotel"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['hotel'].name
        context['rooms'] = Room.objects.filter(hotel=context['hotel'])

        return context
