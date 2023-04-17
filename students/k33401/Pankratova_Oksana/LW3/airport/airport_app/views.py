from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import *
from .models import *


class FlightAPI(generics.RetrieveAPIView):
    serializer_class = FullFlightSerializer
    queryset = Flight.objects.all()
    # permission_classes = (IsAuthenticated,)


class EmployeeAPI(generics.RetrieveAPIView):
    serializer_class = FullEmployeeSerializer
    queryset = Employee.objects.all()


class PlaneAPI(generics.RetrieveAPIView):
    serializer_class = FullPlaneSerializer
    queryset = Plane.objects.all()


class FlightListAPI(generics.ListAPIView):
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()


class EmployeeListAPI(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class PlaneListAPI(generics.ListAPIView):
    serializer_class = PlaneSerializer
    queryset = Plane.objects.all()


class FlightCreateAPI(generics.CreateAPIView):
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()


class EmployeeCreateAPI(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class PlaneCreateAPI(generics.CreateAPIView):
    serializer_class = PlaneSerializer
    queryset = Plane.objects.all()


class TransitLandingCreateAPI(generics.CreateAPIView):
    serializer_class = TransitLandingSerializer
    queryset = TransitLanding.objects.all()


class FlightUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()


class EmployeeUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class PlaneUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlaneSerializer
    queryset = Plane.objects.all()






