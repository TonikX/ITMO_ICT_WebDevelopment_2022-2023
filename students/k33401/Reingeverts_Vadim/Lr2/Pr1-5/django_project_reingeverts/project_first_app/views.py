from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Car, Ownership, CarOwner, DriverLicense


def car_owner_detail(request, car_owner_pk):
    try:
        car_owner = CarOwner.objects.get(pk=car_owner_pk)
    except CarOwner.DoesNotExist:
        raise Http404("Car does not exist")

    return render(request, 'owner.html', {'car_owner': car_owner})
