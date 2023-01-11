from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from .models import Owner, Car
from .forms import OwnerForm


def owner_detail(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': p})


def owner_all(request):
    context = {}
    context["dataset"] = Owner.objects.all()

    return render(request, "owner_all.html", context)


class CarList(ListView):
    model = Car
    template_name = 'car_all.html'


class CarRetrieveView(DetailView):
    model = Car
    template_name = 'car.html'


def create_owner(request):
    context = {}

    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_owner.html", context)


class CarUpdate(UpdateView):
  model = Car
  fields = ['number', 'brand', 'model', 'color']
  template_name = 'update_car.html'
  success_url = '/all_cars/'


class CarCreate(CreateView):
  model = Car
  template_name = 'create_car.html'
  fields = ['number', 'brand', 'model', 'color']


class CarDelete(DeleteView):
  model = Car
  template_name = 'delete_car.html'
  success_url = '/all_cars/'
