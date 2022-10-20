from django.shortcuts import render
from .models import Driver
from .models import Car
from django.views.generic.list import ListView


def index(request):
    return render(request, "index.html")


# def get_driver(request, id):
#     try:
#         d = Driver.objects.get(pk=id)
#     except Driver.DoesNotExist:
#         raise Http404("Poll does not exist")
#     return render(request, 'driver.html', {'driver': d})


def get_driver(request):
    driver_id = request.GET.get('id')
    if driver_id:
        context = {"driver": 1, "dataset": Driver.objects.get(pk=driver_id)}
    else:
        context = {"driver": 0, "dataset": Driver.objects.all()}
    return render(request, "driver.html", context)


def get_drivers(request):
    context = {"driver": 0, "dataset": Driver.objects.all()}
    return render(request, "driver.html", context)


class CarList(ListView):
    template_name = 'car.html'
    car = Car
    queryset = car.objects.all()

    def get_queryset(self):
        car_id = self.request.GET.get('id')
        if car_id:
            try:
                car_id = int(car_id)
                queryset = self.queryset.filter(id=car_id)
            except ValueError:
                queryset = self.model.objects.none()
            return queryset
        return self.queryset
