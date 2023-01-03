from typing import List
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Country, Tourist, Tour, Reservation, Comment
from .forms import LoginForm, UserRegistrationForm

def show_tour(request, tour_id):
    try:
        tour = Tour.objects.get(pk=tour_id)
        comments = Comment.objects.filter(tour_id=tour)
    except Tour.DoesNotExist:
        raise Http404
    return render(request, 'tour.html', {'tour': tour, 'comments': comments})


class All_Tours(ListView):
    model = Tour
    template_name = 'all_tour.html'

    @staticmethod
    def all_countries():
        return Country.objects.all()


class All_Tours_Registered(ListView):
    model = Tour
    template_name = 'tour_registered.html'

    @staticmethod
    def all_countries():
        return Country.objects.all()

def tours_registered(request, tour_id):
    try:
        tour = Tour.objects.get(pk=tour_id)
        comments = Comment.objects.filter(tour_id=tour)
    except Tour.DoesNotExist:
        raise Http404
    return render(request, 'all_tour_registered.html', {'tour': tour, 'comments': comments})

def tour_filter_registered(request, pk):
    tours = Tour.objects.all().filter(country_id=pk)
    return render(request, 'filter.html', {'tours': tours}) 

def tour_filter(request, pk):
    tours = Tour.objects.all().filter(country_id=pk)
    return render(request, 'filter_nr.html', {'tours': tours}) 

class Tourist_Page(ListView):
    model = Tourist
    template_name = 'tourist_page.html'

class All_Reservations(ListView):
    model = Reservation
    template_name = 'all_reservation.html'

class Make_Reservation(CreateView):
    model = Reservation
    template_name = 'reservation_create.html'
    fields = ['tourist_id', 'tour_id']
    success_url = '/home/registered'


class Edit_Reservation(UpdateView):
    model = Reservation
    template_name = 'reservation_edit.html'
    fields = ['tourist_id', 'tour_id']
    success_url = '/home/registered'

class Delete_Reservation(DeleteView):
    model = Reservation
    template_name = 'reservation_delete.html'
    success_url = '/home/registered'


class All_Comments(ListView):
    model = Comment
    template_name = 'all_comment.html'


class All_Comments_Registered(ListView):
    model = Comment
    template_name = 'all_comment_registered.html'


class Leave_Comment(CreateView):
    model = Comment
    template_name = 'comment.html'
    fields = ['tourist_id', 'tour_id', 'text', 'rate']
    success_url = '/tour/registered'


class Home(ListView):
    model = Tour
    template_name = 'home.html'


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/home/registered')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form}) 


def logout_user(request):
    logout(request)
    return redirect('/home/')