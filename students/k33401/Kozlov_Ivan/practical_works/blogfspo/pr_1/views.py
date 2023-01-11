from django.http import Http404
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from pr_1.forms import Transport_owner_form
from pr_1.models import Driver_doc, Ownership, Transport, Transport_owner


def get_index(request):
    return render(request, "templates/index.html")


def get_info_transport_owner(request, id_owner):
    try:
        owner = Transport_owner.objects.get(pk=id_owner)

    except Transport_owner.DoesNotExist:
        raise Http404("does not exist")

    return render(request, "templates/owner.html", {"owner": owner})


def get_all_owners(request):
    return render(
        request, "templates/all_owners.html", {"all_owners": Transport_owner.objects.all()}
    )


class all_cars(ListView):
    model = Transport
    template_name = "all_cars.html"


class get_car_by_id(DetailView):
    model = Transport
    template_name = "get_cars.html"


def create_view(request):
    context = {}
    form = Transport_owner_form(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "create_view.html", context)


class Update_trancpoty(UpdateView):
    model = Transport
    fields = [
        "model_car",
        "color",
        "marka",
        "gov_number",
    ]
    success_url = "/all_cars/"
    template_name = "update_car.html"


class Create_car(CreateView):
    model = Transport
    fields = [
        "id_car",
        "model_car",
        "color",
        "marka",
        "gov_number",
    ]
    success_url = "/all_cars/"
    template_name = "create_car.html"


class Delete_car(DeleteView):
    model = Transport
    success_url = "/all_cars/"
    template_name = "delete_car.html"


class Create_owner_user(CreateView):
    model = Transport_owner
    fields = [
        "username",
        "password",
        "id_owner",
        "last_name",
        "first_name",
        "date_birthday",
        "passport_number",
        "home_adress",
        "national",
        "email",
    ]
    success_url = "/all_owners/"
    template_name = "create_new_owner.html"
