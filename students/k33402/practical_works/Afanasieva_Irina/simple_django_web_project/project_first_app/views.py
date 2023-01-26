from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from project_first_app.models import Owner, Car
from project_first_app.forms import OwnerForm


def owner(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'owner.html', {'owner': owner})


def owners_list(request):
    try:
        all_owners = Owner.objects.all()
        context = {}
        context["dataset"] = all_owners
    except Owner.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'owners_list.html', context)


class CarsList(ListView):
    model = Car
    template_name = 'cars_list.html'


class CarsDetail(DetailView):
    model = Car
    template_name = 'car_detail.html'


def create_owner(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'create_owner.html', context)


class CarCreate(CreateView):
    model = Car
    template_name = 'car_create.html'
    fields = [
        "car_number",
        "car_make",
        "car_model",
        "car_color",
    ]
    success_url = '/cars_list'


class CarUpdate(UpdateView):
    model = Car
    template_name = 'car_update.html'
    fields = [
        "car_number",
        "car_make",
        "car_model",
        "car_color",
    ]
    success_url = '/cars_list'


class CarDelete(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars_list'


