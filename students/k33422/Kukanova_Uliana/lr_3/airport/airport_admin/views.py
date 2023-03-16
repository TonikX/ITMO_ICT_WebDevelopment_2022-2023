from rest_framework import generics

from airport_admin.serializers import *


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class AirplaneListView(generics.ListAPIView):
    serializer_class = AirplaneSerializer

    def get_queryset(self):
        queryset = Airplane.objects.all()
        maintenance_param = self.request.query_params.get('under_maintenance')

        if maintenance_param:
            queryset = queryset.filter(under_maintenance=maintenance_param)

        return queryset


class AirplaneCreateView(generics.CreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer


class AirplaneModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer


class ScheduleListView(generics.ListAPIView):
    queryset = FlightAsScheduled.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleCreateView(generics.CreateAPIView):
    queryset = FlightAsScheduled.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlightAsScheduled.objects.all()
    serializer_class = ScheduleSerializer


class FlightListView(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def get_queryset(self):
        queryset = Flight.objects.all()
        number = self.request.query_params.get('number', None)

        if number:
            queryset = queryset.filter(number=number)

        return queryset


class FlightCreateView(generics.CreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class AirlineAdministrationListView(generics.ListAPIView):
    queryset = AirlineAdministration.objects.all()
    serializer_class = AirlineAdministrationSerializer


class AirlineAdministrationCreateView(generics.CreateAPIView):
    queryset = AirlineAdministration.objects.all()
    serializer_class = AirlineAdministrationSerializer


class AirlineAdministrationModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AirlineAdministration.objects.all()
    serializer_class = AirlineAdministrationSerializer


class TransitListView(generics.ListAPIView):
    queryset = Transit.objects.all()
    serializer_class = TransitSerializer


class TransitCreateView(generics.CreateAPIView):
    queryset = Transit.objects.all()
    serializer_class = TransitSerializer


class TransitModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transit.objects.all()
    serializer_class = TransitSerializer
