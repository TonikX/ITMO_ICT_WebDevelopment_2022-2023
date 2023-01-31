from django.http import Http404 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.shortcuts import render, redirect
from project_first_app.models import *
from project_first_app.forms import *


def list_view(request):
    owners = Owner.objects.all().exclude(username='admin')
    ctx = {'owners': owners}

    return render(request, 'owners/view_owners.html', ctx)


def detail(request, pk):
    try:
        owner_m = Owner.objects.get(pk=pk)
        license_m = License.objects.filter(owner=owner_m).last()
        cars_m = Property.objects.filter(owner=owner_m, end_date=None)
        ctx = {'owner': owner_m, 'cars': cars_m, 'license': license_m}
    except Owner.DoesNotExist:
        raise Http404(f"Owner with id {pk} does not exist")
    return render(request, 'owners/view_owner.html', ctx)


class CarListView(ListView):
    model = Car
    template_name = 'cars/view_cars.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/view_car.html'


def create_owner(request):
    ctx = {}

    form = OwnerForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/owner/')
    ctx['form'] = form
    return render(request, "owners/create.html", ctx)


class CarCreateView(CreateView):
    model = Car
    fields = ['number', 'manufacturer', 'model', 'color']
    success_url = '/car/'
    template_name = 'cars/create.html'


class CarUpdateView(UpdateView):
    model = Car
    fields = ['number', 'manufacturer', 'model', 'color']
    success_url = '/car/'
    template_name = 'cars/create.html'


class CarDeleteView(DeleteView):
    model = Car
    success_url = '/car/'
    template_name = 'cars/delete.html'