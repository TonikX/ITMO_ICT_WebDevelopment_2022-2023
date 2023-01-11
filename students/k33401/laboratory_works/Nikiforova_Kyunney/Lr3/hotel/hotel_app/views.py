from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


class GuestListView(generics.ListAPIView):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()


class GuestCreateView(generics.CreateAPIView):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()


class GuestUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()


class GuestDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()


class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeCreateView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Guest.objects.all()


class EmployeeUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class CleaningListView(generics.ListAPIView):
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()


class CleaningCreateView(generics.CreateAPIView):
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()


class CleaningUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()


class CleaningDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()


class RoomListView(generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomCreateView(generics.CreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class BookingUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class BookingDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()