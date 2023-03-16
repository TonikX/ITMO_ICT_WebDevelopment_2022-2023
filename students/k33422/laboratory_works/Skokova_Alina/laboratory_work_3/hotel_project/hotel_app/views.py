from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from .serializers import *


class BookingRoomDatesListAPIView(generics.ListAPIView):
    serializer_class = BookingAndClientSerializer

    def get_queryset(self):
        id_room = self.kwargs['id_room']
        room_chosen = Room.objects.get(id_room=id_room)
        date_start = self.kwargs['date_start']
        date_end = self.kwargs['date_end']
        queryset = Booking.objects.filter(
            id_room=room_chosen, date_start__range=[date_start, date_end]) | Booking.objects.filter(
            id_room=room_chosen, date_end__range=[date_start, date_end]) | Booking.objects.filter(
            id_room=room_chosen, date_start__lte=date_start, date_end__gte=date_end) | Booking.objects.filter(
            id_room=room_chosen, date_start__lte=date_start, date_end__isnull=True)
        return queryset
    
class ClientListAPIView(generics.ListAPIView):
    serializer_class = ClientSerializer

    def get_queryset(self):
        city = self.kwargs['city']
        queryset = Client.objects.filter(city=city)
        return queryset

class CleanerGetAPIView(generics.ListAPIView):
    serializer_class = ScheduleAndCleanerSerializer
    
    def get_queryset(self):
        day = self.kwargs['day']
        id_room = self.kwargs['id_room']
        room_chosen = Room.objects.get(id_room=id_room)
        queryset = Schedule.objects.filter(day=day, id_floor=room_chosen.id_floor)
        return queryset

class RoomVacantListAPIView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        booked_ids = []
        for i in Booking.objects.filter(date_end__isnull=True):
            booked_ids.append(i.id_room.id_room)
        return Room.objects.exclude(id_room__in=booked_ids)

class BookingAndClientListAPIView(generics.ListAPIView):
    serializer_class = BookingAndClientSerializer

    def get_queryset(self):
        passport = self.kwargs['passport']
        client_chosen = Client.objects.get(passport=passport)
        return Booking.objects.filter(id_client=client_chosen)

class BookingDatesListAPIView(generics.ListAPIView):
    serializer_class = BookingAndClientSerializer

    def get_queryset(self):
        date_start = self.kwargs['date_start']
        date_end = self.kwargs['date_end']
        queryset = Booking.objects.filter(
            date_start__range=[date_start, date_end]) | Booking.objects.filter(
            date_end__range=[date_start, date_end]) | Booking.objects.filter(
            date_start__lte=date_start, date_end__gte=date_end) | Booking.objects.filter(
            date_start__lte=date_start, date_end__isnull=True)
        return queryset

class CleanerCreateView(generics.CreateAPIView):
    serializer_class = CleanerCreateSerializer
    queryset = Cleaner.objects.all()

class CleanerDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = CleanerSerializer
    queryset = Cleaner.objects.all()

class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingCreateSerializer
    queryset = Booking.objects.all()

class BookingUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

class ScheduleCreateView(generics.CreateAPIView):
    serializer_class = ScheduleCreateSerializer
    queryset = Schedule.objects.all()

class ScheduleGetView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScheduleAndCleanerSerializer
    queryset = Schedule.objects.all()

class CleanerAndScheduleListAPIView(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        id_cleaner = self.kwargs['id_cleaner']
        cleaner_chosen = Cleaner.objects.get(id_cleaner=id_cleaner)
        return Schedule.objects.filter(id_cleaner=cleaner_chosen)

class RoomsPerFloor(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        id_floor = self.kwargs['id_floor']
        floor_chosen = Floor.objects.get(id_floor=id_floor)
        return Room.objects.filter(id_floor=floor_chosen)