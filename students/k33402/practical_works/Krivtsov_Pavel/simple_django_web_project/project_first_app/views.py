from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import CarOwner, Car


def owner_details(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("This car owner does not exist")

    return render(request, 'owner.html', {'owner': owner})


def owners_list(request):
    context = {"owners": CarOwner.objects.all()}
    return render(request, 'owners_list.html', context)


class CarList(ListView):
    model = Car
    template_name = "car_list.html"

class CarRetrieveView(DetailView):
    model = Car
