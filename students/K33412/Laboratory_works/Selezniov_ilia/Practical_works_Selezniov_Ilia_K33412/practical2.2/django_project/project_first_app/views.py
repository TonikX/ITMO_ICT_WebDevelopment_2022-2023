from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from project_first_app.models import Owner, Car
from .forms import AddCarForm
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView
from django.views.generic.edit import DeleteView


class OwnerUpdateView(UpdateView):
    model = Owner
    fields = ['first_name', 'last_name', 'date_of_birth']
    success_url = '/owners'
    template_name = 'update_template.html'


class CarUpdateView(UpdateView):
    model = Car
    fields = ['brand', 'model', 'color', 'plate_number']
    success_url = '/cars'
    template_name = 'update_template.html'


def owner(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404('Owner does not exist')

    return render(request, 'specific_owner.html', {"Owner": owner})


def car(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        raise Http404('Owner does not exist')

    return render(request, 'specific_car.html', {"Car": car})


class OwnersList(ListView):
    model = Owner
    template_name = 'owners_list.html'


class CarsList(ListView):
    model = Car
    template_name = 'cars_list.html'


def createCar(request):
    context = {}

    form = AddCarForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form

    return render(request, "create_car.html", context)


class OwnerCreateView(CreateView):

    # specify the model for create view
    model = Owner
    template_name = 'create_owner.html'

    # specify the fields to be displayed

    fields = ['first_name', 'last_name', 'date_of_birth']
    success_url = '/owners'


class OwnerDeleteView(DeleteView):
    model = Owner
    success_url = '/owners'
    template_name = 'owner_delete.html'


class CarDeleteView(DeleteView):
    model = Car
    success_url = '/cars'
    template_name = 'car_delete.html'
