from django.shortcuts import render
from django.http import Http404

from .models import Owner


def get_info_owner(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)

    except Owner.DoesNotExist:
        raise Http404("Does not exist!")

    return render(request, "templates/owner.html", {"owner": owner})


def get_all_owners(request):
    return render(request, "all_owners.html", {"all_owners": Owner.objects.all()})

