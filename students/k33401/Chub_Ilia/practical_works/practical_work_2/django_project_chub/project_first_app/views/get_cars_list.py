from ..models import Car
from django.views.generic import ListView


class GetCarsList(ListView):
    model = Car
    template_name = 'cars_list.html'
