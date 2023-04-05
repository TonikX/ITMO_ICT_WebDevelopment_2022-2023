from django.http import Http404
from django.shortcuts import render
from project_first_app.models import CarOwner, Car
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import CarOwnerCreateForm


def index(request):
    return render(request, 'index.html')

def owner_detail(request, id_owner):
    try:
        owner = CarOwner.objects.get(pk=id_owner)
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner_detail.html', {'owner': owner})

def owner_list(request):
    context = {}
    context['owners'] = CarOwner.objects.all()

    return render(request, 'owner_list.html', context)

def owner_create(request):
    context = {}

    form = CarOwnerCreateForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "owner_create.html", context)


class CarList(ListView):
    model = Car
    template_name = 'car_list.html'

class CarDetail(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarUpdate(UpdateView):
    model = Car
    fields = ['gov_number', 'brand', 'model', 'color']
    success_url = '/car/'
    template_name = 'car_update.html'

class CarCreate(CreateView):
   model = Car
   template_name = 'car_create.html'
   fields = ['gov_number', 'brand', 'model', 'color']

class CarDelete(DeleteView):
   model = Car
   template_name = 'car_delete.html'
   success_url = '/car/'
