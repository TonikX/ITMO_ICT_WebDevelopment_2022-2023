from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView

from .forms import *
from .models import *


class ReserveView(CreateView):
    form_class = ReserveForm
    template_name = 'reserve.html'

    def post(self, request, *args, **kwargs):
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            print(request)
            return redirect('hotels')
        return render(request, 'error.html')


class CommentView(CreateView):
    form_class = CommentForm
    template_name = 'comment.html'

    def get_context_data(self, **kwargs):
        context = super(CommentView, self).get_context_data(**kwargs)
        context['hotel'] = Hotel.objects.get(pk=self.kwargs['id_hotel'])
        context['room_type'] = RoomType.objects.get(pk=self.kwargs['id_rt'])
        context['room'] = Room.objects.get(pk=self.kwargs['id_room'])
        return context

    def get(self, request, *args, **kwargs):
        form = CommentForm()
        context = {'form': form,
                   'hotel': Hotel.objects.get(pk=self.kwargs['id_hotel']),
                   'room_type': RoomType.objects.get(pk=self.kwargs['id_rt']),
                   'room': Room.objects.get(pk=self.kwargs['id_room'])}
        return render(request, 'comment.html', context)

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            print(request)
            return redirect('room', id_hotel=self.kwargs['id_hotel'], id_rt=self.kwargs['id_rt'], pk=self.kwargs['id_room'])
        return render(request, 'error.html')


class RoomView(DetailView):
    model = Room
    template_name = 'room.html'
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super(RoomView, self).get_context_data(**kwargs)
        context['hotel'] = Hotel.objects.get(pk=self.kwargs['id_hotel'])
        context['room_type'] = RoomType.objects.get(pk=self.kwargs['id_rt'])
        context['comments'] = Comment.objects.filter(id_room=self.kwargs['pk'])
        return context


class RoomListView(ListView):
    model = Room
    template_name = 'rooms.html'
    context_object_name = 'rooms'

    def get_context_data(self, **kwargs):
        context = super(RoomListView, self).get_context_data(**kwargs)
        context['hotel'] = Hotel.objects.get(pk=self.kwargs['id_hotel'])
        context['room_type'] = RoomType.objects.get(pk=self.kwargs['id_rt'])
        return context

    def get_queryset(self):
        return Room.objects.filter(id_rt=self.kwargs['id_rt'])


class HotelView(DetailView):
    model = Hotel
    template_name = 'hotel.html'
    context_object_name = 'hotel'

    def get_context_data(self, **kwargs):
        context = super(HotelView, self).get_context_data(**kwargs)
        context['room_types'] = RoomType.objects.filter(id_hotel=self.kwargs['pk'])
        return context


class HotelListView(ListView):
    model = Hotel
    template_name = 'hotels.html'
    context_object_name = 'hotels'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HotelListView, self).get_context_data(**kwargs)
        return context
