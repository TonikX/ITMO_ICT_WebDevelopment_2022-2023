from ..models import Car
from django.views.generic import UpdateView


class UpdateCarInfo(UpdateView):
    model = Car
    fields = ['state_number', 'brand', 'model', 'color']
    template_name = 'car_updation_form.html'
    success_url = '/cars/all'
