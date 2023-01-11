from django.shortcuts import render #импортирует метод, который "запускает" созданную html страницу и передает в нее указанные параметры
from django.http import Http404 #импортирует метод обработки ситуации, когда нет необходимых записей в бд (обработчик ошибок)
from project_first_app.models import Owner, Car 
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .forms import OwnerForm

def owner(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': owner})

def owners(request):
    return render(request, 'owners.html', {'owners': Owner.objects.all()})

def create_owner(request):
    data = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'owner_create.html', data)


class CarList(ListView):
    model = Car
    template_name = 'car_list.html'

class CarUpdate(UpdateView):
    model = Car
    fields = ['state_num', 'stamp', 'model', 'color']
    template_name = 'car_update.html'
    success_url = '/car_list'

class CarCreate(CreateView):
    model = Car
    fields = ['state_num', 'stamp', 'model', 'color']
    template_name = 'car_create.html'
    success_url = '/car_list'

class CarDelete(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/car_list'