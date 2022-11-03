from django.http import Http404
from django.shortcuts import render
from .models import CarOwner


def owner_details(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("This car owner does not exist")

    return render(request, 'owner.html', {'owner': owner})


def owners_list(request):
    context = {"owners": CarOwner.objects.all()}
    return render(request, 'owners_list.html', context)
