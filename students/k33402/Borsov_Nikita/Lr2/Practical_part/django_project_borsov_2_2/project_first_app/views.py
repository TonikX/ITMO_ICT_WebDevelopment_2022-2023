from django.http import Http404
from django.shortcuts import render
from project_first_app.models import Property
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Car
from .forms import OwnerForm


def car_info(request, car_id):
    try:
        car_properties = Property.objects.filter(car_id=car_id)
        car_first_owner = car_properties.order_by('start_date')[0].owner_id
    except Exception as e:
        raise Http404(e)
    return render(request, 'carInfo.html', {'car_id': car_id, 'car_first_owner': car_first_owner})


def car_info_full(request, car_id):
    try:
        car_properties = Property.objects.filter(car_id=car_id)
    except Exception as e:
        raise Http404(e)
    return render(request, 'carAllOwners.html', {'car_id': car_id, 'car_properties': car_properties})


class CarsRetrieveView(ListView):
    model = Car
    template_name = 'carsDetails.html'


class CarRetrieveView(DetailView):
    model = Car
    template_name = 'oneCarDetails.html'


def create_new_owner(request):
    if request.method == "POST":
        form = OwnerForm(request.POST)
        print(vars(form))
        if form.is_valid():
            print("VALID")
            form.save()
    form = OwnerForm()
    data = {
        'form': form,
    }
    return render(request, 'createOwner.html', data)


class CarUpdateView(UpdateView):
    model = Car
    fields = ['state_number', 'car_brand', 'car_model', 'car_color']
    template_name = 'carInfoUpdateForm.html'
    success_url = '/carsInfo'


class CarCreateView(CreateView):
    model = Car
    fields = ['state_number', 'car_brand', 'car_model', 'car_color']
    template_name = 'carInfoCreateForm.html'
    success_url = '/carsInfo'


class CarDeleteView(DeleteView):
    model = Car
    fields = []
    template_name = 'carInfoDeleteForm.html'
    success_url = '/carsInfo'


