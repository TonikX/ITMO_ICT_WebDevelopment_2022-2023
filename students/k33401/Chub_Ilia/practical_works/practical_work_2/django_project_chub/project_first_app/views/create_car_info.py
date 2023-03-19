from ..models.car import Car
from django.views.generic import CreateView


class CreateCarInfo(CreateView):
    model = Car
    fields = ['id', 'state_number', 'brand', 'model', 'color']
    template_name = 'car_creation_form.html'
    success_url = '/cars/all'
