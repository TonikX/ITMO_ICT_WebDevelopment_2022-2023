from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import OwnerForm
from .models import Owner, Auto


def get_car_owner(request, id_owner: int):
    # https:..owner/1/
    try:
        owner = Owner.objects.get(pk=id_owner)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist.")
    return render(request, 'owner.html', {'owner': owner})

def get_all_owners(request):
    return render(request, 'all_owners.html', {'all_owners': Owner.objects.all()})

class AutoList(ListView):
    # list view
    model = Auto
    template_name = 'all_autos.html'

class AutoRetrieveView(DetailView):
    # detail view
  model = Auto
  template_name = 'auto_detail.html'


def create_owner(request):
    # form of creating object owner
    context = {}
    form = OwnerForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_owner.html", context)

class AutoCreate(CreateView):
  model = Auto
  template_name = 'create_auto.html'
  fields = ['number', 'mark', 'model', 'color']
  success_url = '/all_autos/'

class AutoDelete(DeleteView):
    model = Auto
    template_name = 'delete_auto.html'
    success_url = '/all_autos/'

class AutoUpdate(UpdateView):
    model = Auto
    fields = ['number', 'mark', 'model', 'color']
    template_name = 'update_auto.html'
    success_url = '/all_autos/'

class CreateOwnerForm(CreateView):
    model = Owner
    fields = [
        "username",
        "password",

        "last_name",
        "first_name",
        "date_birth",
        "passport",
        "address",
        "national",
    ]
    success_url = "/owners/"
    template_name = "create_owner.html"