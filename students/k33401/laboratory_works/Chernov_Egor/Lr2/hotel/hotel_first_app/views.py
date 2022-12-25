from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView

from .forms import *
from .models import *


class ReserveRoomView(CreateView):
    form_class = ReserveForm
    template_name = 'reserve.html'

    def get(self, request, *args, **kwargs):
        self.initial = {'name_hotel': Hotel.objects.get(pk=self.kwargs.get('id_hotel')).name_hotel,
                        'room_number': Room.objects.get(pk=self.kwargs.get('id_room')).number_room}
        return super(ReserveRoomView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = ReserveForm(request.POST)
        try:
            id_hotel = Hotel.objects.get(name_hotel=form.data.get('name_hotel')).id_hotel
            room = Room.objects.get(id_hotel=id_hotel, number_room=form.data.get('room_number'))
        except:
            return render(request, 'error.html')

        if form.is_valid():
            response = form.save(commit=False)
            response.id_guest = self.request.user
            response.id_room = room
            form.save()
            return redirect('hotels')
        return render(request, 'error.html')


class ReserveView(CreateView):
    form_class = ReserveForm
    template_name = 'reserve.html'

    def post(self, request, *args, **kwargs):
        form = ReserveForm(request.POST)
        try:
            id_hotel = Hotel.objects.get(name_hotel=form.data.get('name_hotel')).id_hotel
            room = Room.objects.get(id_hotel=id_hotel, number_room=form.data.get('room_number'))
        except:
            return render(request, 'error.html')

        if form.is_valid():
            response = form.save(commit=False)
            response.id_guest = self.request.user
            response.id_room = room
            form.save()
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
