from django.shortcuts import render
from django.http import Http404
from .models import CarOwner, Car
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .forms import CreateCarOwner


# Create your views here.


def info_about_car_owner(request, id):
    try:
        owner = CarOwner.objects.get(pk=id)
    except CarOwner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'owner.html', {'owner': owner})


def owners(request):
    return render(request, 'owners.html', {'owners': CarOwner.objects.all()})


class CarsList(ListView):
    model = Car
    template_name = 'cars.html'


class CarById(DetailView):
    model = Car
    template_name = 'car.html'


def create_car_owner(request):
    data = {}
    form = CreateCarOwner(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'create_car_owner.html', data)


class CarCreate(CreateView):
    model = Car
    fields = ['car_id', 'state_number', 'make_car', 'model_car', 'colour']
    template_name = 'create_car.html'
    success_url = '/cars/'


class CarUpdate(UpdateView):
    model = Car
    fields = ['car_id', 'state_number', 'make_car', 'model_car', 'colour']
    template_name = 'update_car.html'
    success_url = '/cars/'


class CarDelete(DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = '/cars/'
