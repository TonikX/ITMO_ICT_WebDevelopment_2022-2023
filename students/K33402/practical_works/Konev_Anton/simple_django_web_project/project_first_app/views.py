from django.shortcuts import render
from django.http import Http404
from django.views.generic import *
from .models import *
from .forms import *


# Create your views here.
def details(request, owner_id):
    try:
        car_owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'car_owner.html', {'car_owner': car_owner})


def owners_list(request):
    return render(request, 'owners_list.html', {'all_owners': CarOwner.objects.all()})


def create_owner(request):
    form = CreateOwner(request.POST or None)

    if form.is_valid():
        form.save()
        form = CreateOwner()

    return render(request, 'create_owner.html', {'form': form})


class CarsListView(ListView):
    model = Car
    template_name = 'cars_list.html'


class CarRetrieveView(DetailView):
    model = Car
    template_name = 'car.html'


class CarCreateView(CreateView):
    model = Car
    template_name = 'create_car.html'
    fields = ['car_id', 'number_plate', 'brand', 'model', 'color']
    success_url = '/cars_list/'


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'update_car.html'
    fields = ['number_plate', 'color']
    success_url = '/cars_list/'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = '/cars_list/'
