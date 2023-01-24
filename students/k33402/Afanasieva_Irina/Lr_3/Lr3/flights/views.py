from django.shortcuts import render
from rest_framework import generics
from flights.serializers import *


class PassengerListView(generics.ListAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class PassengerCreateView(generics.CreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerCreateSerializer


class PassengerEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerCreateSerializer


class PlaneListView(generics.ListAPIView):
    serializer_class = PlaneSerializer

    def get_queryset(self):
        queryset = Plane.objects.all()
        params = self.request.query_params

        company = params.get('company', None)
        if company:
            queryset = queryset.filter(company=company)

        return queryset


class PlaneCreateView(generics.CreateAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneCreateSerializer


class PlaneEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneCreateSerializer


class FlightListView(generics.ListAPIView):
    serializer_class = FlightSerializer

    def get_queryset(self):
        queryset = Flight.objects.all()
        params = self.request.query_params

        wherefrom = params.get('from', None)
        whereto = params.get('to', None)
        if wherefrom:
            queryset = queryset.filter(wherefrom=wherefrom)
        if whereto:
            queryset = queryset.filter(whereto=whereto)

        return queryset
            

class FlightCreateView(generics.CreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightCreateSerializer


class FlightEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightCreateSerializer


class TicketListView(generics.ListAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        queryset = Ticket.objects.all()
        params = self.request.query_params

        passenger = params.get('passenger', None)
        if passenger:
            queryset = queryset.filter(passenger=passenger)

        return queryset


class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateSerializer


class TicketEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateSerializer


class AirCompanyListView(generics.ListAPIView):
    queryset = AirCompany.objects.all()
    serializer_class = AirCompanySerializer


class AirCompanyCreateView(generics.CreateAPIView):
    queryset = AirCompany.objects.all()
    serializer_class = AirCompanySerializer


class AirCompanyEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AirCompany.objects.all()
    serializer_class = AirCompanySerializer
