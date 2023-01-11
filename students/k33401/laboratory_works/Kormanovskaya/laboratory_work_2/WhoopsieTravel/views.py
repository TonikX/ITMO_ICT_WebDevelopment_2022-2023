import datetime

from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView

from .models import Country, Tour, TourImage, TourConducting
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateCustomerForm, BookingForm


def countries_list(request):
    countries = Country.objects.all()
    return render(request, 'WhoopsieTravel/countries.html', context={'countries': countries})


@login_required(login_url='login_url')
def country_details(request, slug):
    country = Country.objects.get(slug__iexact=slug)
    tours = Tour.objects.filter(country__name=country.name)
    for t in tours:
        images = TourImage.objects.filter(tour__title=t.title)
        t.images = images
    return render(request, 'WhoopsieTravel/country_details.html', context={'country': country, 'tours': tours})


def tours_list(request):
    tours = Tour.objects.all()
    for t in tours:
        images = TourImage.objects.filter(tour__title=t.title)
        t.images = images
    return render(request, 'WhoopsieTravel/tours.html', context={'tours': tours})


@login_required(login_url='login_url')
def tour_details(request, slug):
    tour = Tour.objects.get(slug__iexact=slug)
    rates = TourConducting.objects.filter(tour__title=tour.title).exclude(rate=None)
    images = TourImage.objects.filter(tour__title=tour.title)
    tour.images = images

    form = BookingForm(request.POST or None)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_url')

    isOrdered = TourConducting.objects.filter(customer__username=request.user.username, tour__title=tour.title,
                                              date_start__gt=datetime.date.today())

    return render(request, 'WhoopsieTravel/tour_details.html',
                  context={'tour': tour, 'form': form, 'ordered': isOrdered, 'rates': rates})


def registration(request):
    if request.user.is_authenticated:
        return redirect('tours_list_url')
    else:
        form = CreateCustomerForm()

        if request.method == 'POST':
            form = CreateCustomerForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))

                return redirect('login_url')

        return render(request, 'WhoopsieTravel/registration.html', context={'form': form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('tours_list_url')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile_url')
            else:
                messages.info(request, 'Username OR password is incorrect')

        return render(request, 'WhoopsieTravel/login.html', context={})


def logout_user(request):
    logout(request)
    return redirect('login_url')


@login_required(login_url='login_url')
def profile(request):
    tour_conducting = TourConducting.objects.filter(customer__username__iexact=request.user)
    tour_conducting = tour_conducting.order_by('date_start').reverse()
    return render(request, 'WhoopsieTravel/profile.html',
                  context={'tc': tour_conducting, 'today': datetime.date.today()})


def sells(request):
    tour_conducting = TourConducting.objects.filter(is_paid=True).order_by('date_start').reverse()
    return render(request, 'WhoopsieTravel/sells.html', context={'tc': tour_conducting})


class ReviewUpdate(UpdateView):
    model = TourConducting
    fields = ['review_text', 'rate']
    success_url = '/travel/profile'
    template_name = 'WhoopsieTravel/review.html'


class TourConductingDelete(DeleteView):
    model = TourConducting
    template_name = 'WhoopsieTravel/reserve_delete.html'
    success_url = '/travel/profile'


class TourConductingUpdate(UpdateView):
    model = TourConducting
    fields = ['date_start', 'contact_info', 'tourists']
    success_url = '/travel/profile'
    template_name = 'WhoopsieTravel/reserve_update.html'
