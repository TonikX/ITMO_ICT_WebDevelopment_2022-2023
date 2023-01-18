from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import TypeRoom, Client, Room, Employee, Booking
from rest_framework import serializers, generics, status
from rest_framework.response import Response
from .serializers import *
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db.models import Count


class AllClients(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]


class CreateClient(generics.CreateAPIView, generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class UpdateClient(generics.RetrieveUpdateAPIView):
      serializer_class = ClientSerializer
      queryset = Client.objects.all()


class DeleteClient(generics.RetrieveDestroyAPIView):
      serializer_class = ClientSerializer
      queryset = Client.objects.all()

###


class AllWorkers(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = WorkersSerializer
    permission_classes = [IsAuthenticated]


class CreateWorker(generics.CreateAPIView, generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = WorkersSerializer


class EmployeeUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = WorkersSerializer
    queryset = Employee.objects.all()


class EmployeeDestroy(generics.RetrieveDestroyAPIView):
    serializer_class = WorkersSerializer
    queryset = Employee.objects.all()

###

class AllRooms(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]


class CreateRoom(generics.CreateAPIView, generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomDelete(generics.RetrieveDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

###


class AllBook(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class CreateBook(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class UpdateBook(generics.RetrieveUpdateAPIView):
    serializer_class = BookSerializer
    queryset = Booking.objects.all()


class DeleteBook(generics.RetrieveDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Booking.objects.all()

###


class AllBookWithInfo(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookSerializerWithInfoAboutRoomAndTypeRoom


class RoomCount(generics.ListAPIView):
    serializer_class = RoomCountSerializer

    def get_queryset(self):
        c = Room.objects.annotate(num_rooms=Count('id_room')).count()
        return [{'count': c}]


class ClientCount(generics.ListAPIView):
    serializer_class = ClientCountSerializer

    def get_queryset(self):
        c = Client.objects.annotate(num_clients=Count('passport')).count()
        queryset = [{'count': c}]
        return queryset



