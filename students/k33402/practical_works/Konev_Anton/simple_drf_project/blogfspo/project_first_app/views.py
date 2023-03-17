from django.shortcuts import render
from django.http import Http404
from .models import Car_owner, Car
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .forms import CreateOwner


# Create your views here.
def details(request, id_owner):
    try:
        owner = Car_owner.objects.get(pk=id_owner)
    except Car_owner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'car_owner.html', {'owner': owner})


def owners_list(request):
    return render(request, 'owners_list.html', {'all_owners': Car_owner.objects.all()})


class CarsListView(ListView):
    model = Car
    template_name = 'cars_list.html'


class CarRetrieveView(DetailView):
    model = Car
    template_name = 'car.html'


def create_owner(request):
    data = {}
    form = CreateOwner(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'create_owner.html', data)


class CarUpdateView(UpdateView):
    model = Car
    fields = ['number_plate', 'color']
    template_name = 'update_car.html'
    success_url = '/cars_list/'


class CarCreateView(CreateView):
    model = Car
    fields = ['id_car', 'number_plate', 'brand', 'model', 'color']
    template_name = 'create_car.html'
    success_url = '/cars_list/'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = '/cars_list/'
