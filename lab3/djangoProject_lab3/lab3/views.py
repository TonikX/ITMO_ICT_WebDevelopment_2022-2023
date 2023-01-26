from django.http import Http404
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from .models import Driver, Car


# Create your views here.


def detail(request, driver_id):
    try:
        driver = Driver.objects.get(pk=driver_id)
    except Driver.DoesNotExist:
        raise Http404("Driver does not exist")
    return render(request, '../templates/owner.html', {'driver': driver})


def all_owners(request):
    try:
        drivers = Driver.objects.all()
    except Driver.DoesNotExist:
        raise Http404("Driver does not exist")
    return render(request, '../templates/all_owners.html', {'drivers': drivers})


def all_cars(request):
    try:
        cars = Car.objects.all()
    except Driver.DoesNotExist:
        raise Http404("Driver does not exist")
    return render(request, '../templates/all_cars.html', {'cars': cars})


class DriverCreateView(CreateView):
    model = Driver
    fields = ['username','password','first_name','last_name','passport', 'address', 'nationality']
    success_url = '/allowners/'


class CarCreateView(CreateView):
    model = Car
    fields = ['number', 'marka', 'model', 'color']
    success_url = '/allcars/'


class CarUpdateView(UpdateView):
    model = Car
    fields = ['number', 'marka', 'model', 'color']
    success_url = '/allcars/'


class CarDeleteView(DeleteView):
    model = Car
    success_url = '/allcars/'
