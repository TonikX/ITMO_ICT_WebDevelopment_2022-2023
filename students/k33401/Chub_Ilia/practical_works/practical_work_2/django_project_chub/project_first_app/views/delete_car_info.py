from ..models.car import Car
from django.views.generic import DeleteView


class DeleteCarInfo(DeleteView):
    model = Car
    template_name = 'car_deletion_form.html'
    success_url = '/cars/all'
