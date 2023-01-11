from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from .models import Driver, Vehicle
from .forms import DriverForm


def driver(request, driver_id):
    try:
        d = Driver.objects.get(pk=driver_id)
    except Driver.DoesNotExist:
        raise Http404('Driver does not exist')
    return render(request, 'driver.html', {'driver': d})


def drivers(request):
    context = {'dataset': Driver.objects.all()}
    return render(request, "drivers.html", context)


def create_driver(request):
    context = {}
    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'create_driver.html', context)


class VehicleList(ListView):
    model = Vehicle
    template_name = 'vehicles.html'


class VehicleUpdate(UpdateView):
    model = Vehicle
    fields = ['number', 'brand', 'model', 'color']
    success_url = '/vehicles'
    template_name = 'vehicle_form.html'


class VehicleCreate(CreateView):
    model = Vehicle
    fields = ['number', 'brand', 'model', 'color']
    template_name = 'vehicle_form.html'


class VehicleDelete(DeleteView):
    model = Vehicle
    template_name = 'vehicle_confirm_delete.html'
    success_url = '/vehicles'
