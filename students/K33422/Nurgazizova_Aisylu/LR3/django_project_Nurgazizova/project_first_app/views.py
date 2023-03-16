from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from project_first_app.models import OwnerUser, Car
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from .forms import OwnerForm

# Create your views here.
def owner(request, pk):
    try:
        owner = OwnerUser.objects.get(pk=pk)
    except OwnerUser.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, "project_first_app/owner.html", {'dataset':owner})

def owners(request):
    context = {}
    context["dataset"] = OwnerUser.objects.all()

    form = OwnerForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "project_first_app/owners.html", context)

class CarList(ListView):
  model = Car
  template_name = 'project_first_app/car_list.html'

class CarViev(DetailView):
  model = Car

class CarUpdateView(UpdateView):
  model = Car
  fields = ['gos_number', 'mark', 'model', 'color']
  success_url = '/car/list/'

class CarCreateView(CreateView):
    model = Car
    fields = ['gos_number', 'mark', 'model', 'color']
    success_url = '/car/list/'

class CarDeleteView(DeleteView):
    model = Car
    success_url = '/car/list/'