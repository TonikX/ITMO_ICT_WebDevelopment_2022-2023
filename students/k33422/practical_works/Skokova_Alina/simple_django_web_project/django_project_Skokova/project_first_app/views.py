from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from .forms import *
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

def car_owner_info(request, id_owner):
    try:
        c = CarOwner.objects.get(pk=id_owner)
    except CarOwner.DoesNotExist:
        raise Http404("Car Owner does not exist")
    return render(request, 'owner.html', {'owner': c})

def list_view_owners(request):
    dataset = CarOwner.objects.all()
    return render(request, 'list_view_owners.html', {'dataset': dataset})

class CarsList(ListView):
    model = Car
    template_name = "list_view_cars.html"

class CarInfo(DetailView):
    model = Car

def create_owner_view(request):
    context ={}

    form = CarOwnerForm(request.POST or None) 
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_owner_view.html", context)

class CarUpdateView(UpdateView):
    model = Car
    fields = ['state_num', 'brand', 'model', 'color']
    success_url = '/cars_list/'

class CarCreateView(CreateView):
    model = Car
    fields = ['state_num', 'brand', 'model', 'color']
    success_url = '/cars_list/'

class CarDeleteView(DeleteView):
    model = Car
    success_url = '/cars_list/'