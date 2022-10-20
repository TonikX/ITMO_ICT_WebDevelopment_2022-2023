from .models import transport_Owner, Transport
from django.http import Http404
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView


def get_info_transport_owner(request, id_owner):
    try:
        owner = transport_Owner.objects.get(pk=id_owner)
    except transport_Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'templates/owner.html', {'owner': owner})


def get_all_owners(request):
    context = {"get_all_owners": transport_Owner.objects.all()}
    return render(
        request, "templates/get_all_owners.html", context
    )


def get_all_cars(request):
    context = {"get_all_cars": Transport.objects.all()}
    return render(
        request, "templates/get_all_cars.html", context
    )


class update_car_info(UpdateView):
    model = Transport
    fields = [
        "brand",
        "car_model",
        "colour",
        "registration_plate",
    ]
    success_url = "/get_all_cars/"
    template_name = "update_car_info.html"


class get_car_by_id(DetailView):
    model = Transport
    template_name = "get_car_by_id.html"


class create_new_owner(CreateView):
    model = transport_Owner
    fields = ['id_owner', 'second_name', 'first_name', 'DOB', 'passport_data', 'email', 'nationality', 'home_adress']

    success_url = "/get_all_owners/"
    template_name = "create_new_owner.html"


class create_new_car(CreateView):
    model = Transport
    fields = ['brand', 'car_model', 'colour', 'registration_plate']

    success_url = "/get_all_cars/"
    template_name = "create_new_car.html"


class delete_car(DeleteView):
    model = Transport
    success_url = "/get_all_cars/"
    template_name = "delete_car.html"
