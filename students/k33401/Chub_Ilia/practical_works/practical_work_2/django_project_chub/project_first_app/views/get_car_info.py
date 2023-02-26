from . import *
from ..models import Car
from django.views.generic import DetailView


class GetCarInfo(DetailView):
    model = Car
    template_name = 'car_info.html'
