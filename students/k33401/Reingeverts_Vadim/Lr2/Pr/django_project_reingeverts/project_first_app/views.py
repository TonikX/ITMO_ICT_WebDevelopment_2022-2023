from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Car, CarOwner, Ownership, DriverLicense


def car_owner_detail(request, car_owner_pk):
    try:
        car_owner = CarOwner.objects.get(pk=car_owner_pk)
    except CarOwner.DoesNotExist:
        raise Http404("Car does not exist")

    return render(request, 'car_owner_detail.html', {'car_owner': car_owner, 'title': "Car Owner Details"})


def ownership_detail(request, owner_pk):
    try:
        ownership = Ownership.objects.get(pk=owner_pk)
    except Ownership.DoesNotExist:
        raise Http404("Ownership does not exist")

    return render(request, 'ownership_detail.html', {'ownership': ownership, 'title': "Ownership Details"})
