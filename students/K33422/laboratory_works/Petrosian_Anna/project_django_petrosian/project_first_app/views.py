from django.shortcuts import render , get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from project_first_app.form import OwnerForm
from .models import Owner, Car

def all_owners_detail(request):
    context = {"owners": Owner.objects.all(), "all": True}

    return render(request, 'owners.html', context)


def owner_detail(request, owner_id):
    context = get_object_or_404(Owner, pk=owner_id)

    return render(request, 'owners.html', {"owner": context, "one": True})


def create_owner(request):
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/owners')
    return render(request, "owners.html", {"form": form, "new": True})


class AllCars(ListView):
    model = Car
    template_name = "cars.html"


class OneCar(DetailView):
    model = Car
    template_name = "cars.html"


class CarDelete(DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    success_url = '/cars/'


class CarCreate(CreateView):
    model = Car
    template_name = 'car_create_update.html'
    fields = ['id_number', 'brand', 'car_model', 'color', 'official_number']
    success_url = '/cars/'


class CarUpdate(UpdateView):
    model = Car
    fields = ['id_number', 'brand', 'car_model', 'color', 'official_number']
    success_url = '/cars/'
    template_name = 'car_create_update.html'
# Create your views here.