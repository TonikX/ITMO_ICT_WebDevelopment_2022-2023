from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from .models import Worker, Airplane, Flight
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
# Create your views here.


class WorkerCreate(generics.CreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkerDelete(generics.DestroyAPIView):
    queryset = Worker.objects.all()


class WorkerUpdate(generics.UpdateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkerListView(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class AirplaneBrandList(generics.ListAPIView):
    queryset = Airplane.objects.values("brand")
    serializer_class = AirplaneSerializer


class FrequentPlane(APIView):
    # марка самолета, которая чаще всего летает по маршруту
    def get(self, request):
        airp = request.query_params.get('airports')
        airp1 = str(airp)[:3]
        airp2 = str(airp)[3:]
        queryset = Flight.objects.filter(airport_start=airp1, airport_fin=airp2)\
            .values("plane_number__brand")\
            .annotate(Count("plane_number__brand"))\
            .order_by("-plane_number__brand__count")[0]
        # serializer = FlightSerializer(queryset)
        return Response(queryset)


class RepairAirplanes(APIView):
# определить количество самолетов, находящихся в ремонте
    def get(self, request):
        queryset = Airplane.objects.filter(status='REPAIR')\
            .aggregate(Count("plane_number"))
        # serializer = RepairAirplanesSerializer(queryset)
        return Response(queryset)


class WorkersNumber(APIView):
# определить количество работников компании-авиаперевозчика
    def get(self, request):
        company = request.query_params.get('employer')
        queryset = Worker.objects.filter(employer=company)\
            .aggregate(Count("worker_id"))
        # serializer = WorkersNumberSerializer(queryset)
        return Response(queryset)
        # return Response({"Number of workers:": serializer.data})


class AirplaneBrand(APIView):
# общее количество бортов по каждой марке
    def get(self, request):
        queryset = Airplane.objects.values('brand').annotate(Count('plane_number'))
        # serializer = AirplaneBrandSerializer(queryset)
        return Response(queryset)
        # return Response({'brand': [brand for brand in queryset], 'number_of_planes': [plane_number__count for plane_number__count in queryset]})