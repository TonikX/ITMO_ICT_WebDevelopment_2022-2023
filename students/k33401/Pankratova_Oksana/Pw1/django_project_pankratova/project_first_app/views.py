from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from .forms import ExampleForm

# Create your views here.
from django.http import Http404
from .models import Motorist, Automobile


def detail(request, motorist_id):
    try:
        m = Motorist.objects.get(pk=motorist_id)
    except Motorist.DoesNotExist:
        raise Http404("Motorist does not exist")
    return render(request, 'owner.html', {
        'owner': m})


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization [en]
    # добавление данных об объектах, полученных в результате выполнения запроса exampleModel.objects.all() в словарь
    context["dataset"] = Motorist.objects.all()

    return render(request, "list_view.html", context)


class AutoList(ListView):
    # specify the model for list view
    model = Automobile
    template_name = 'auto_list_view.html'


class AutoDetail(DetailView):
    model = Automobile


def create_view(request):
    context = {}

    form = ExampleForm(
        request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


class AutoUpdateView(UpdateView):
    model = Automobile
    fields = ['gos_number', 'color']
    success_url = '/auto/list/'


class AutoCreateView(CreateView):
    model = Automobile
    fields = ['gos_number', 'mark', 'model', 'color']
    success_url = '/auto/list/'


class AutoDeleteView(DeleteView):
    model = Automobile
    success_url = '/auto/list/'
