from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Car, Owner, Ownership, DriverLicense
from .forms import CreateOwner


def get_owner(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(
        request, 'owner.html', {'owner': owner}
    )


def get_all_owners(request):
    context = {"data": Owner.objects.all()}
    return render(request, 'owners.html', context)


def create_owner(request):
    form = CreateOwner(request.POST or None)
    if form.is_valid():
        form.save()
    data = {"form": form}
    return render(request, 'owner_form.html', data)


class Cars(ListView):
    model = Car
    template_name = 'cars.html'


class CarView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarCreate(CreateView):
    model = Car
    fields = ['state_number', 'brand', 'model', 'color']
    template_name = 'car_form.html'
    success_url = '/car/'


class CarUpdate(UpdateView):
    model = Car
    fields = ['state_number', 'brand', 'model', 'color']
    template_name = 'car_form.html'
    success_url = '/car/'


class CarDelete(DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    success_url = '/car/'
