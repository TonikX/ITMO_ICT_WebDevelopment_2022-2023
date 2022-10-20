from django.http import Http404
from django.shortcuts import render
from practical_work_1.models import Car, Owner, Ownership, DriverLicense


def detail(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Car does not exist")
    return render(
        request, 'owner.html', {'owner': owner}
    )
