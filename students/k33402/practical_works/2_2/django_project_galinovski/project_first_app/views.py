from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Owner, Car
from .forms import OwnerForm

class CarList(ListView):
    model = Car
    template_name = 'car_all.html'

class CarRetrieveView(DetailView):
    model = Car
    template_name = 'car.html'

def owner_detail(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': p})

def owner_all(request):
    context = {}
    context["dataset"] = Owner.objects.all()

    return render(request, "owner_all.html", context)

def create_view(request):
    context = {}

    form = OwnerForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class CarUpdateView(UpdateView):
  model = Car
  fields = ['number', 'brand', 'model', 'color']
  template_name = 'car_form.html'
  success_url = '/car/'

class CarCreate(CreateView):
  model = Car
  template_name = 'car_create_view.html'

  fields = ['number', 'brand', 'model', 'color']

class CarDeleteView(DeleteView):
  model = Car
  template_name = 'car_confirm_delete.html'
  success_url = '/car/'