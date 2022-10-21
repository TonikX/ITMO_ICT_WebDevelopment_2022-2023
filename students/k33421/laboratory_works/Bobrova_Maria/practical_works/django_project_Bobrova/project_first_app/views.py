# Create your views here.

from django.shortcuts import render #импортирует метод, который "запускает" созданную хтмл страницу и передает в нее указанные параметры
from django.http import Http404
from .models import Car_owner, Car, Ownerdhip, Driver_license #импортирует таблицу Poll из модели данных models, где polls - название приложения (и папки)


def info_about_car_owner(request, id_owner):
    try:
        owner = Car_owner.objects.get(pk=id_owner)
    except Car_owner.DoesNotExist:
        raise Http404("Car owner does not exist")
    return render(request, 'owner.html', {'owner': owner})

def all_owners(request):
    return render(request, "list_owners.html", {'all_owners' : Car_owner.objects.all()})




