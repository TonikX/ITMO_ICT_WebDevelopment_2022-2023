from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Owner, Ownership, Car, DrivingLicense
from .forms import *
'''
def get_info_owner(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)

    except Owner.DoesNotExist:
        raise Http404("Does not exist!")

    return render(request, "templates/owner.html", {"owner": owner})


def get_info_all_owners(request):
    return render(request, "templates/all_owners.html", {"all_owners": Owner.objects.all()})


def get_info_car(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)

    except Car.DoesNotExist:
        raise Http404("Does not exist!")

    return render(request, "templates/car.html", {"car": car})


def get_info_all_cars(request):
    return render(request, "templates/all_cars.html", {"all_cars": Car.objects.all()})'''


class IndexView(TemplateView):
    template_name = "index.html"


class OwnerRetrieveView(DetailView):
    model = Owner
    template_name = "owner_detail.html"


class OwnerListView(ListView):
    model = Owner
    template_name = "owner_list.html"


class OwnerUpdateView(UpdateView):
    model = Owner
    fields = ["surname", "name", "birthday_date"]
    success_url = "/owner/list/"
    template_name = "owner_update.html"


class OwnerCreateView(CreateView):
    model = Owner
    fields = ["surname", "name", "birthday_date"]
    success_url = "/owner/list/"
    template_name = "owner_create.html"


class OwnerDeleteView(DeleteView):
    model = Owner
    success_url = "/owner/list/"
    template_name = "owner_confirm_delete.html"


class CarRetrieveView(DetailView):
    model = Car
    template_name = "car_detail.html"


class CarListView(ListView):
    model = Car
    template_name = "car_list.html"


class CarUpdateView(UpdateView):
    model = Car
    fields = ["number", "brand", "model", "color"]
    success_url = "/car/list/"
    template_name = "car_update.html"


class CarCreateView(CreateView):
    model = Car
    fields = ["number", "brand", "model", "color"]
    success_url = "/car/list/"
    template_name = "car_create.html"


class CarDeleteView(DeleteView):
    model = Car
    success_url = "/car/list/"
    template_name = "car_confirm_delete.html"


def create_view(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "create_view.html", context)