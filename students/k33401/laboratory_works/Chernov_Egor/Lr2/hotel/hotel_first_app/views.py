from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView

from .forms import CommentForm
from .models import *
# from account.models import User


class CommentView(CreateView):
    form_class = CommentForm
    template_name = 'comment.html'
    # fields = ['rating_c', 'review_c', 'check_in', 'check_out']

    def get_context_data(self, **kwargs):
        context = super(CommentView, self).get_context_data(**kwargs)
        context['hotel'] = Hotel.objects.get(pk=self.kwargs['id_hotel'])
        context['room_type'] = RoomType.objects.get(pk=self.kwargs['id_rt'])
        context['room'] = Room.objects.get(pk=self.kwargs['id_room'])
        return context

    # def get(self, request, *args, **kwargs):
    #     pass

    def post(self, request, *args, **kwargs):
        form = CommentForm()
        form.fields['id_guest'].initial = request.user.username
        form.fields["id_room"].initial = self.kwargs['id_room']
        print(form.fields)
        # form = CommentForm(initial={})
        # context = {'hotel': self.kwargs['id_hotel'],
        #            'room_type': self.kwargs['id_rt'],
        #            'room': self.kwargs['id_room']}
        if form.is_valid():
            form.save()
            return render(request, 'room.html')
        return render(request, 'error.html')

    # def get_success_url(self):
    #     return f"/hotels/hotels/{self.kwargs['id_hotel']}/{self.kwargs['id_rt']}/rooms/{self.kwargs['id_room']}/comment/"


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
