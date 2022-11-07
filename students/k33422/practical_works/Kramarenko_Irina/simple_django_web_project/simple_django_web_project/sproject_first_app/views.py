from django.shortcuts import render #метод, который запускаеи хтмл страницу и передает в нее параметры
from django.http import Http404 # метод обработки ситуации, когда нет необходимых записей в бд
from .models import Owner, Car # таблица из модели данных
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .forms import CreateOwner

# Create your views here.
def detail(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': owner})

def list_owners(request):
    context = {}
    context["dataset"] = Owner.objects.all()

    return render(request, "list_owners.html", context)

def create_owner(request):
    context = {}
    form = CreateOwner(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'create_owner.html', context)

class CarByID(DetailView):
    model = Car
    template_name = "car_detail.html"

class CarsList(ListView):
    model = Car
    template_name = "list_cars.html"

class UpdateCar(UpdateView):
    model = Car
    fields = ['reg_number', 'brand', 'model', 'color']
    template_name = "update_car.html"
    success_url = "/list_cars/"

class FormUpdateCar(UpdateView):
    model = Car
    fields = ['reg_number', 'brand', 'model', 'color']
    template_name = "form_update_car.html"
    success_url = "/list_cars/"

class CreateCar(CreateView):
    model = Car
    fields = ['reg_number', 'brand', 'model', 'color']
    template_name = "create_car.html"
    success_url = "/list_cars/"

class DeleteCar(DeleteView):
    model = Car
    template_name = "delete_car.html"
    success_url = "/list_cars/"