# Лабораторная работа 3

models.py

```
from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    id = models.AutoField(unique=True, primary_key=True)
    passport = models.CharField(max_length=10, verbose_name='Паспортные данные', unique=True)
    full_name = models.CharField(max_length=120, null=False, verbose_name='ФИО')
    age = models.IntegerField(verbose_name='Возраст', default=18)
    education = models.CharField(choices=[('СПО', 'среднее профессиональное'), ('ВО', 'высшее')], max_length=3,
                                 verbose_name='Образование')
    experience = models.IntegerField(verbose_name='Стаж работы в годах')
    in_crew = models.IntegerField(verbose_name='Состоит в экипаже под номером', default=0)

    REQUIRED_FIELDS = ['email', 'full_name', 'experience']

    def __str__(self):
        return "{}".format(self.full_name)


class Airplane(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    tail_number = models.CharField(max_length=8, verbose_name="Номер самолета", unique=True)
    type = models.CharField(max_length=20, verbose_name="Тип")
    seats = models.IntegerField(verbose_name="Число мест")
    velocity = models.IntegerField(verbose_name="Скорость полёта (км/ч)")
    airline = models.CharField(max_length=30, verbose_name="Авиакомпания")
    under_maintenance = models.BooleanField(default=False, verbose_name="В ремонте")

    def __str__(self):
        return "{}".format(self.tail_number)


class FlightAsScheduled(models.Model):
    number = models.IntegerField(unique=True, primary_key=True, verbose_name="Номер рейса")
    distance = models.IntegerField(verbose_name="Расстояние до пункта назначения в км")
    departure = models.CharField(max_length=25, verbose_name="Пункт вылета")
    arrival = models.CharField(max_length=25, verbose_name="Пункт назначения")
    transit = models.ForeignKey('Transit', verbose_name="Транзит", null=True, blank=True, on_delete=models.CASCADE)
    completed = models.IntegerField(verbose_name="Количество совершённых рейсов")

    def __str__(self):
        return "{}, {} -> {}".format(self.number, self.departure, self.arrival)


class Transit(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    destination = models.CharField(max_length=25, verbose_name="Пункт пересадки")

    def __str__(self):
        return "{}".format(self.destination)


class Flight(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    number = models.ForeignKey('FlightAsScheduled', verbose_name="Номер рейса", on_delete=models.CASCADE)
    plane_id = models.ForeignKey('Airplane', verbose_name="Самолёт", on_delete=models.CASCADE)
    crew = models.IntegerField(verbose_name="Экипаж на борту")
    tickets_sold = models.IntegerField(verbose_name="Количество проданных билетов")
    departure_date = models.DateField(verbose_name="Дата вылета")
    departure_time = models.TimeField(verbose_name="Время вылета")
    arrival_date = models.DateField(verbose_name="Дата прилета")
    arrival_time = models.TimeField(verbose_name="Время прилета")
    transit_arrival_date = models.DateField(verbose_name="Дата транзитной посадки", blank=True, null=True)
    transit_arrival_time = models.TimeField(verbose_name="Время транзитной посадки", blank=True, null=True)
    transit_departure_date = models.DateField(verbose_name="Дата вылета из транзита", blank=True, null=True)
    transit_departure_time = models.TimeField(verbose_name="Время вылета из транзита", blank=True, null=True)

    def __str__(self):
        return "{}-{}".format(self.number, self.plane_id)


class AirlineAdministration(models.Model):
    employee = models.ForeignKey('Employee', verbose_name="ФИО сотрудника", on_delete=models.CASCADE)
    job = models.CharField(max_length=30, verbose_name="Должность")
    clearance = models.BooleanField(default=True, verbose_name="Допуск")
```

urls.py

```
from django.urls import path
from .views import *

urlpatterns = [
    path('client/', ClientListAPIView.as_view()),
    path('client/create/', ClientCreateAPIView.as_view()),
    path('client/<int:pk>/', ClientRUDAPIView.as_view()),

    path('servicespl/', ServicesPLListAPIView.as_view()),
    path('servicespl/create/', ServicesPLCreateAPIView.as_view()),
    path('servicespl/<int:pk>/', ServicesPLRUDAPIView.as_view()),

    path('materialspl/', MaterialsPLListAPIView.as_view()),
    path('materialspl/create/', MaterialsPLCreateAPIView.as_view()),
    path('materialspl/<int:pk>/', MaterialsPLRUDAPIView.as_view()),

    path('request/', RequestListAPIView.as_view()),
    path('request/create/', RequestCreateAPIView.as_view()),
    path('request/<int:pk>/', RequestRUDAPIView.as_view()),
    path('request/nested/', RequestNestedAPIView.as_view()),

    path('executor/', ExecutorListAPIView.as_view()),
    path('executor/create/', ExecutorCreateAPIView.as_view()),
    path('executor/<int:pk>/', ExecutorRUDAPIView.as_view()),

    path('chosenservices/', ChosenServicesListAPIView.as_view()),
    path('chosenservices/create/', ChosenServicesCreateAPIView.as_view()),
    path('chosenservices/<int:pk>/', ChosenServicesRUDAPIView.as_view()),
    path('chosenservices/full/', ChosenServicesFullListAPIView.as_view()),

    path('chosenmaterials/', ChosenMaterialsListAPIView.as_view()),
    path('chosenmaterials/create/', ChosenMaterialsCreateAPIView.as_view()),
    path('chosenmaterials/<int:pk>/', ChosenMaterialsRUDAPIView.as_view()),
    path('chosenmaterials/full/', ChosenMaterialsFullListAPIView.as_view()),

    path('workgroup/', WorkGroupListAPIView.as_view()),
    path('workgroup/create/', WorkGroupCreateAPIView.as_view()),
    path('workgroup/<int:pk>/', WorkGroupRUDAPIView.as_view()),
    path('workgroup/full/', WorkGroupFullListAPIView.as_view()),

    path('invoice/', InvoiceListAPIView.as_view()),
    path('invoice/create/', InvoiceCreateAPIView.as_view()),
    path('invoice/<int:pk>/', InvoiceRUDAPIView.as_view()),

    path('paymentorder/', PaymentOrderListAPIView.as_view()),
    path('paymentorder/create/', PaymentOrderCreateAPIView.as_view()),
    path('paymentorder/<int:pk>/', PaymentOrderRUDAPIView.as_view()),
]
```

view.py

```
@@ -0,0 +1,279 @@
from .serializer import *
from rest_framework import generics


# Create your views here.

# Client
class ClientListAPIView(generics.ListAPIView):

    serializer_class = ClientViewSerializer

    def get_queryset(self):
        queryset = Client.objects.all()
        params = self.request.query_params

        legal_entity = params.get('legal_entity', None)

        if legal_entity:
            queryset = queryset.filter(legal_entity=legal_entity)

        return queryset


class ClientCreateAPIView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer


class ClientRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientViewSerializer


# ServicesPL
class ServicesPLListAPIView(generics.ListAPIView):
    serializer_class = ServicesPLWTypeViewSerializer

    def get_queryset(self):
        queryset = ServicesPL.objects.all()
        params = self.request.query_params

        service_type = params.get('service_type', None)

        if service_type:
            queryset = queryset.filter(service_type=service_type)

        return queryset


class ServicesPLCreateAPIView(generics.CreateAPIView):
    queryset = ServicesPL.objects.all()
    serializer_class = ServicesPLCreateSerializer


class ServicesPLRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicesPL.objects.all()
    serializer_class = ServicesPLViewSerializer


# MaterialsPL
class MaterialsPLListAPIView(generics.ListAPIView):
    queryset = MaterialsPL.objects.all()
    serializer_class = MaterialsPLViewSerializer


class MaterialsPLCreateAPIView(generics.CreateAPIView):
    queryset = MaterialsPL.objects.all()
    serializer_class = MaterialsPLCreateSerializer


class MaterialsPLRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaterialsPL.objects.all()
    serializer_class = MaterialsPLViewSerializer


# Request
class RequestListAPIView(generics.ListAPIView):
    serializer_class = RequestWStatusViewSerializer

    def get_queryset(self):
        queryset = Request.objects.all()
        params = self.request.query_params

        status = params.get('status', None)
        from_date = params.get('from_date', None)
        to_date = params.get('to_date', None)
        legal_entity = params.get('legal_entity', None)

        if status:
            queryset = queryset.filter(status=status)

        if from_date:
            queryset = queryset.filter(req_date__gte=from_date)

        if to_date:
            queryset = queryset.filter(req_date__lte=to_date)

        if legal_entity:
            queryset = queryset.filter(client__legal_entity=legal_entity)

        return queryset


class RequestCreateAPIView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestCreateSerializer


class RequestRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestViewSerializer


class RequestNestedAPIView(generics.ListAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestNestedSerializer


# ChosenServices
class ChosenServicesListAPIView(generics.ListAPIView):
    serializer_class = ChosenServicesWSRViewSerializer

    def get_queryset(self):
        queryset = ChosenServices.objects.all()
        params = self.request.query_params

        req = params.get('req', None)

        if req:
            queryset = queryset.filter(req=req)

        return queryset


class ChosenServicesCreateAPIView(generics.CreateAPIView):
    queryset = ChosenServices.objects.all()
    serializer_class = ChosenServicesCreateSerializer


class ChosenServicesRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChosenServices.objects.all()
    serializer_class = ChosenServicesViewSerializer


class ChosenServicesFullListAPIView(generics.ListAPIView):
    queryset = ChosenServices.objects.all()
    serializer_class = ChosenServicesNestedSerializer


# ChosenMaterials
class ChosenMaterialsListAPIView(generics.ListAPIView):
    serializer_class = ChosenMaterialWMRsViewSerializer

    def get_queryset(self):
        queryset = ChosenMaterials.objects.all()
        params = self.request.query_params

        req = params.get('req', None)

        if req:
            queryset = queryset.filter(req=req)

        return queryset


class ChosenMaterialsCreateAPIView(generics.CreateAPIView):
    queryset = ChosenMaterials.objects.all()
    serializer_class = ChosenMaterialsCreateSerializer


class ChosenMaterialsRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChosenMaterials.objects.all()
    serializer_class = ChosenMaterialsViewSerializer


class ChosenMaterialsFullListAPIView(generics.ListAPIView):
    queryset = ChosenMaterials.objects.all()
    serializer_class = ChosenMaterialsNestedSerializer


# WorkGroup
class WorkGroupListAPIView(generics.ListAPIView):
    serializer_class = WorkGroupWREViewSerializer

    def get_queryset(self):
        queryset = WorkGroup.objects.all()
        params = self.request.query_params

        req = params.get('req', None)
        executor = params.get('executor', None)
        start_date = params.get('start_date', None)
        end_date = params.get('end_date', None)

        if req:
            queryset = queryset.filter(req=req)

        if executor:
            queryset = queryset.filter(executor=executor)

        if start_date:
            queryset = queryset.filter(start_date__gte=start_date)

        if end_date:
            queryset = queryset.filter(end_date__lte=end_date)

        return queryset


class WorkGroupCreateAPIView(generics.CreateAPIView):
    queryset = WorkGroup.objects.all()
    serializer_class = WorkGroupCreateSerializer


class WorkGroupRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkGroup.objects.all()
    serializer_class = WorkGroupViewSerializer


class WorkGroupFullListAPIView(generics.ListAPIView):
    queryset = WorkGroup.objects.all()
    serializer_class = WorkGroupNestedSerializer


# Executor
class ExecutorListAPIView(generics.ListAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorViewSerializer


class ExecutorCreateAPIView(generics.CreateAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorCreateSerializer


class ExecutorRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorViewSerializer


# Invoice
class InvoiceListAPIView(generics.ListAPIView):
    serializer_class = InvoiceViewNestedSerializer

    def get_queryset(self):
        queryset = Invoice.objects.all()
        params = self.request.query_params

        legal_entity = params.get('legal_entity', None)

        if legal_entity:
            queryset = queryset.filter(client__legal_entity=legal_entity)

        return queryset


class InvoiceCreateAPIView(generics.CreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceCreateSerializer


class InvoiceRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceViewSerializer


# PaymentOrder
class PaymentOrderListAPIView(generics.ListAPIView):
    queryset = PaymentOrder.objects.all()
    serializer_class = PaymentOrderNestedSerializer


class PaymentOrderCreateAPIView(generics.CreateAPIView):
    queryset = PaymentOrder.objects.all()
    serializer_class = PaymentOrderCreateSerializer


class PaymentOrderRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentOrder.objects.all()
    serializer_class = PaymentOrderViewSerializer
```

apps.py

```
from django.contrib import admin
from .models import *

admin.site.register(Employee)
admin.site.register(Airplane)
admin.site.register(FlightAsScheduled)
admin.site.register(Transit)
admin.site.register(Flight)
admin.site.register(AirlineAdministration)
```
