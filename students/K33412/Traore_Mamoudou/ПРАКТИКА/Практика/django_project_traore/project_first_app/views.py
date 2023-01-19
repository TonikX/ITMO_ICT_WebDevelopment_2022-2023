from django.shortcuts import render
from django.http import Http404
from project_first_app.models import OwnerUser, Auto
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .forms import OwnerForm


def owner(request, owner_id):
    try:
        owner = OwnerUser.objects.get(pk=owner_id)
    except OwnerForm.DoesNotExist:
        raise Http404('Owner does not exist')

    return render(request, 'owner.html', {'owner': owner})

def owner_create(request):
    data = {}

    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['form'] = form
    return render(request, 'project_first_app/owner_create.html', data)

def list_owners(request):
    owners = {'owners': OwnerUser.objects.all()}
    return render(request, 'list_owners.html', owners)

class AutoList(ListView):
    model = Auto

class AutoCreate(CreateView):
    model = Auto
    template_name = 'project_first_app/auto_create.html'
    fields = ['license_plate', 'brand', 'model', 'color']
    success_url = '/auto/list'

class AutoUpdate(UpdateView):
    model = Auto
    template_name = 'project_first_app/auto_update.html'
    fields = ['license_plate', 'color']
    success_url = '/auto/list'

class AutoDelete(DeleteView):
    model = Auto
    template_name = 'project_first_app/auto_delete.html'
    success_url = '/auto/list'