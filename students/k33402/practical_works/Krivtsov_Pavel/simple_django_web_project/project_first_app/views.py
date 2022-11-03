from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render

from .models import CarOwner, Car
from .forms import CreateOwnerForm


def owner_details(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("This car owner does not exist")

    return render(request, 'owner.html', {'owner': owner})


def owners_list(request):
    context = {"owners": CarOwner.objects.all()}
    return render(request, 'owners_list.html', context)


def create_owner(request):
    form = CreateOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {"form": form}

    return render(request, "create_owner.html", context)


class CarList(ListView):
    model = Car
    template_name = "car_list.html"


class CarRetrieveView(DetailView):
    model = Car


class CarCreate(CreateView):
    model = Car
    template_name = "car_create.html"
    fields = ["state_number", "make", "model", "color"]
    success_url = "/cars"
