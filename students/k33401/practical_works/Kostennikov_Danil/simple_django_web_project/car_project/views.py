from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import *
from .forms import CarOwnerCreateForm

# Create your views here.
class CarList(ListView):
    model = Car
    template_name = 'cars.html'

class CarCreate(CreateView):
    model = Car
    fields = ['car_number', 'brand', 'model', 'color']
    template_name = 'car_create.html'

class CarUpdate(UpdateView):
    model = Car
    fields = ['car_number', 'brand', 'model', 'color']
    success_url = '/cars/'
    template_name = 'car_create.html'

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'
    template_name = "car_delete.html"

def create_owner(request):
    context ={}
    form = CarOwnerCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request, 'owner_create.html',context)

def owners(request):
    context = {'owners': CarOwner.objects.all()}
    return render(request, 'owners.html', context)

def owner(request,id):
    try:
        owner = CarOwner.objects.get(id=id)
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': owner})