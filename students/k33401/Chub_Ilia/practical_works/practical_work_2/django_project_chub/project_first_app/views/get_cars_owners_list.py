from . import *
from ..models import CarOwner


def get_cars_owners_list(request):
    return render(request, 'cars_owners_list.html', {'owners': CarOwner.objects.all()})
