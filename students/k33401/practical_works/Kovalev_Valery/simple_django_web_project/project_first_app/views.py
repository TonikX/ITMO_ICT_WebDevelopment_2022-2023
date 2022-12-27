from django.shortcuts import render
from django.http import Http404
from .models import CarOwner, Own


def car_owner(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
        owns = Own.objects.filter(car_owner=owner)
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exists")
    return render(request, "owner.html", {"owner_info": {"owner": owner, "owns": owns}})
