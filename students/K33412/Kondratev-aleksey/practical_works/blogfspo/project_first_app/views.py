from django.shortcuts import render
from django.http import Http404
from .models import *


def info_about_owner(request, id_owner):
    try:
        owner = CarOwner.objects.get(pk=id_owner)
    except CarOwner.DoesNotExist:
        raise Http404("Owner doesn`t exist")
    return render(request, 'owner.html', {'owner': owner})

def all_owners():
    return render(request, 'list_owners.html', {'all_owners': CarOwner.object.all()})
