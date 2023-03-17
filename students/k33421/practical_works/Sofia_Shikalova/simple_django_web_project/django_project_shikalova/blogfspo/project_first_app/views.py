from django.shortcuts import render
from django.http import Http404
from .models import *
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .forms import CreateOwner


def owner_information(request, id_owner):
    try:
        owner = Owner.objects.get(pk=id_owner)
    except Owner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'owner.html', {'owner': owner})


def return_all_owners(request):
    return render(request, "all_owners.html", {'all_owners' : Owner.objects.all()})


class CarListView(ListView):
    model = Car
    template_name = 'all_cars.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car.html'


def create_owner(request):
    data = {}
    form = CreateOwner(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'create_owner.html', data)


class CarUpdate(UpdateView):
    model = Car
    fields = ['state_number', 'brand', 'model', 'color']
    template_name = 'update_car.html'
    success_url = '/all_cars/'


class CarCreate(CreateView):
    model = Car
    fields = ['id_car', 'state_number', 'brand', 'model', 'color']
    template_name = 'create_car.html'
    success_url = '/all_cars/'


class CarDelete(DeleteView):
    model = Car
    template_name = 'delete_cars.html'
    success_url = '/all_cars/'
