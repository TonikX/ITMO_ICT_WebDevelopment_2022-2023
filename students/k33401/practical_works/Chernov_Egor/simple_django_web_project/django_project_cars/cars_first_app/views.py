# from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Driver


def index(request):
    return render(request, "index.html")


def get_driver(request, id):
    try:
        d = Driver.objects.get(pk=id)
    except Driver.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'driver.html', {'driver': d})
