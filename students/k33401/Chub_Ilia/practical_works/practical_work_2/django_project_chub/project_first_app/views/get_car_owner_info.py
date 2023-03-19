from . import *
from .. models import CarOwner


def get_car_owner_info(request, owner_id) -> HttpResponse:
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Car owner does not exist")

    return render(request, 'car_owner_info.html', {'owner': owner})
