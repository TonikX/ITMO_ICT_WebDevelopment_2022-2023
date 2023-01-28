from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView

from project_first_app.forms import *
from project_first_app.models import *


def list_view(request):
	owners = Owner.objects.all()

	return render(request, 'owners/list_view.html', {'owners': owners})


def detail(request, pk):
	try:
		owner = Owner.objects.get(pk=pk)
		lic = License.objects.filter(owner_id=owner).last()
		vehicles = Property.objects.filter(owner_id=owner, end_date=None)
	except Owner.DoesNotExist:
		raise Http404("Owner does not exist")
	return render(request, 'owners/detail.html', {'owner': owner, 'vehicles': vehicles, 'license': lic})


class VehicleList(ListView):
	model = Vehicle
	template_name = 'vehicles/list_view.html'


class VehicleDetail(DetailView):
	model = Vehicle
	template_name = 'vehicles/detail.html'


def create_owner(request):
	context = {}

	form = OwnerForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('/owner/')
	context['form'] = form
	return render(request, "owners/create_view.html", context)


class VehicleCreate(CreateView):
	model = Vehicle
	fields = ['registration_number', 'manufacturer', 'model', 'color']
	success_url = '/vehicle/'
	template_name = 'vehicles/create_view.html'


class VehicleUpdate(UpdateView):
	model = Vehicle
	fields = ['registration_number', 'manufacturer', 'model', 'color']
	success_url = '/vehicle/'
	template_name = 'vehicles/create_view.html'


class VehicleDelete(DeleteView):
	model = Vehicle
	success_url = '/vehicle/'
	template_name = 'vehicles/delete_view.html'
