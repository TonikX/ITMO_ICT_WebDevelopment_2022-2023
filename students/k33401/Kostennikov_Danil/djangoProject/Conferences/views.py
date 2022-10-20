from django.shortcuts import render
from django.http import Http404
from .models import *

# Create your views here.

def main_page(request):
    n = ["Foo", "Bar"]
    return render(request, 'main_page.html', context={'names': n})

