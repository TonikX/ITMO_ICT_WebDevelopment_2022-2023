from django.shortcuts import render

# Create your views here.

from django.http import Http404
from project_first_app.models import CarOwnerUser, Car
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from project_first_app.forms import CarOwnerCreateForm


def car_owner_info(request, car_owner_id):
    try:
        o = CarOwnerUser.objects.get(pk=car_owner_id)
    except CarOwnerUser.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'owner.html', {'car_owner': o})

def all_owners(request):
    context = {}
    context["owners"] = CarOwnerUser.objects.all()
    return render(request, 'all_owners.html', context)

def car_owner_create(request):
    context = {}
    form = CarOwnerCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "owner_create.html", context)


class AllCars(ListView):
    model = Car
    template_name = 'all_cars.html'


class CarInfo(DetailView):
    model = Car
    template_name = 'car.html'

class CarUpdate(UpdateView):
    model = Car
    template_name = 'car_update.html'
    fields = ['car_number', 'color']
    success_url = '/all_cars/'

class CarCreate(CreateView):
    model = Car
    template_name = 'car_create.html'
    fields = ['car_number', 'brand', 'model', 'color']
    success_url = '/all_cars/'

class CarDelete(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/all_cars/'