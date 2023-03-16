# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics
from .models import *
from .serializers import *


class Clients(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    # permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        client = ClientSerializer(data=request.data)
        if client.is_valid():
            client.save()
            return Response({"status": "Клиент добавлен"})
        else:
            return Response({"status": "Error"})


# class Rooms(APIView):
#     permission_classes = [permissions.IsAuthenticated, ]

#     def get(self, request):
#         rooms = Room.objects.all()
#         serializer = RoomSerializer(rooms, many=True)
#         return Response({"data": serializer.data})


class RoomsVacant(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        booked_ids = []
        for i in Booking.objects.filter(date_end__isnull=True):
            booked_ids.append(i.id_room.id_room)
        rooms = Room.objects.exclude(id_room__in=booked_ids)
        serializer = RoomSerializer(rooms, many=True)
        return Response({"data": serializer.data})


class Cleaners(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        cleaners = Cleaner.objects.all()
        serializer = CleanerSerializer(cleaners, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        cleaner = CleanerSerializer(data=request.data)
        if cleaner.is_valid():
            cleaner.save()
            return Response({"status": "Служащий добавлен"})
        else:
            return Response({"status": "Error"})


class Bookings(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        booking = BookingCreateSerializer(data=request.data)
        if booking.is_valid():
            booking.save()
            return Response({"status": "Клиент заселен"})
        else:
            return Response({"status": "Error"})
        

class Schedules(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        schedules = Schedule.objects.all()
        serializer = ScheduleSerializer(schedules, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        schedule = ScheduleCreateSerializer(data=request.data)
        if schedule.is_valid():
            schedule.save()
            return Response({"status": "Расписание добавлено"})
        else:
            return Response({"status": "Error"})

# class SchedulesByDay(APIView):
#     permission_classes = [permissions.IsAuthenticated, ]

#     def get(self, request):
#         day = request.GET.get("day")
#         schedules = Schedule.objects.filter(day=day)
#         serializer = ScheduleSerializer(schedules, many=True)
#         return Response({"data": serializer.data})


class CleanerDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = CleanerSerializer
    queryset = Cleaner.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]


class BookingUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingCreateSerializer
    queryset = Booking.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]


class ScheduleUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScheduleCreateSerializer
    queryset = Schedule.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]