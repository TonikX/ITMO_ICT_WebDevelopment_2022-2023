# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import Http404
from simple_drf_project.models import Auto, Owner, Ownage, License
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


def autos(request, id):
    try:
        auto = Auto.objects.get(pk=id)
        ownage = Ownage.objects.get_queryset()
        print("OWNAGE!!!", ownage)
        try:
            ownage = Ownage.objects.get(owner_id=owner_id, auto_id__ownage=id)
        except Ownage.DoesNotExist:
            ownage = Ownage.objects.get(owner_id=None)
        print("OWNAGE!!!", ownage)

        context = {
            'id': auto.id,
            'state_num': auto.state_num,
            'brand': auto.brand,
            'model': auto.model,
            'color': auto.color,
            'owner_id': ownage.owner_id,
        }
    except Auto.DoesNotExist:
        raise Http404("This auto does not exist!")

    return render(request, 'automobiles/autos.html', context)


def owners(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)

        context = {
            'id': owner.id,
            'last_name': owner.last_name,
            'first_name': owner.first_name,
            'birthdate': owner.birthdate,
            'full_name': owner.last_name + " " + owner.first_name,
            # 'owns': ownage.auto_id,
        }
    except Owner.DoesNotExist:
        raise Http404("This owner does not exist!")

    return render(request, 'automobiles/owners.html', context)
