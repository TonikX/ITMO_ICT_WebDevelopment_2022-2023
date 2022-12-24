from django.shortcuts import render
from .models import *
from .forms import DriverForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


def index(request):
    return render(request, "index.html")


# def get_driver(request, id):
#     try:
#         d = Driver.objects.get(pk=id)
#     except Driver.DoesNotExist:
#         raise Http404("Poll does not exist")
#     return render(request, 'driver.html', {'driver': d})


def get_driver(request, id):
    try:
        context = {"driver": 1, "dataset": Driver.objects.get(pk=id)}
    except:
        context = {"driver": 0, "dataset": Driver.objects.all()}
    return render(request, "driver.html", context)


def get_drivers(request):
    context = {"driver": 0, "dataset": Driver.objects.all()}
    return render(request, "driver.html", context)


class CarList(ListView):
    template_name = 'car.html'
    car = Car
    queryset = car.objects.all()

    def get_queryset(self):
        car_id = self.request.GET.get('id')
        if car_id:
            try:
                car_id = int(car_id)
                queryset = self.queryset.filter(id=car_id)
            except ValueError:
                queryset = self.model.objects.none()
            return queryset
        return self.queryset


def create_driver(request):
    context = {}
    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'driver_form.html', context)


class CarCreate(CreateView):
    model = Car
    template_name = 'car_form.html'
    fields = ['license_plate', 'car_brand', 'model', 'color']


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_form.html'
    fields = ['license_plate', 'car_brand', 'model', 'color']
    success_url = '/cars/'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    success_url = '/cars/'
