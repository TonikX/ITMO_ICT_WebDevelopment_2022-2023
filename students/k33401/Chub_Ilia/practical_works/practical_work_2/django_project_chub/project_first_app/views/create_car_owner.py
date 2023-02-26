from . import *
from ..forms import CreateCarOwnerForm


def create_car_owner(request):
    data = {}
    form = CreateCarOwnerForm(request.POST or None)

    if form.is_valid():
        form.save()

    data['form'] = form

    return render(request, 'car_owner_creation_form.html', data)
