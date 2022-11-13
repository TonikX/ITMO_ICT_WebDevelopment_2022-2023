from django.shortcuts import render
from django.http import Http404
from .models import CarOwner
# Create your views here.


def info_about_car_owner(request, id):
    try:
        owner = CarOwner.objects.get(pk=id)
    except CarOwner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'owner.html', {'owner': owner})
