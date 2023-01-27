from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from avto.models import Car_owner, Car
from avto.forms import FormAddOwner
from django.views.generic.edit import UpdateView, CreateView, DeleteView

def get_owners(request):
    try:
        owners = {}
        owners['data'] = Car_owner.objects.all()
    except Car_owner.DoesNotExist:
        raise Http404("Owners does not exist")
    return render(request, 'owner.html', owners)

class Car_view(ListView):
    model = Car
    template_name = 'car.html'


def add_owner(request):

    context = {}
    form = FormAddOwner(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "add_owner.html", context)

class CarUpdate(UpdateView):
  model = Car
  template_name = "update_car.html"
  fields = ['state_number', 'mark', 'model', 'color']
  success_url = '/cars'

class CarCreate(CreateView):
  model = Car
  template_name = "create_car.html"
  fields = ['state_number', 'mark', 'model', 'color']
  success_url = '/cars'

class CarDelete(DeleteView):
  model = Car
  template_name = "delete_car.html"
  success_url = '/cars'