from django.http import Http404
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import OwnerForm
from .models import Car, Owner


def owner(request, owner_id):
    try:
        o = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404('Owner does not exist')
    return render(request, 'owner.html', {'owner': o})


def owners(request):
    context = {'dataset': Owner.objects.all()}
    return render(request, "owners.html", context)


def create_owner(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'create_owner.html', context)


class CarList(ListView):
    model = Car
    template_name = 'cars.html'


class CarUpdate(UpdateView):
    model = Car
    fields = ['number', 'brand', 'model', 'color']
    success_url = '/cars'
    template_name = 'car_form.html'


class CarCreate(CreateView):
    model = Car
    fields = ['number', 'brand', 'model', 'color']
    template_name = 'car_form.html'


class CarDelete(DeleteView):
    model = Car
    template_name = 'cars_confirm_delete.html'
    success_url = '/cars'
