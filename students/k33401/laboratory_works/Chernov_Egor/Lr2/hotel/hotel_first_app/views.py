from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from .forms import *
from .models import *


class RoomView(DetailView):
    model = Room
    template_name = 'room.html'
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super(RoomView, self).get_context_data(**kwargs)
        context['hotel'] = Hotel.objects.get(pk=self.kwargs['id_hotel'])
        context['room_type'] = RoomType.objects.get(pk=self.kwargs['id_rt'])
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


class RegView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'index.html'
    success_url = 'hotels'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        context = {'username': ""}
        if form.is_valid():
            form.save()
            context['username'] = form.cleaned_data.get('username')
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            login(request, user)
        return render(request, 'hotels.html', context)


class LogInView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('hotels')


class LogOutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('index')
