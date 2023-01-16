from django.shortcuts import render
from rest_framework.views import APIView
from .models import TypeRoom, Client, PriceConstructor, Room, Workers, Book
from rest_framework import serializers, generics, status
from rest_framework.response import Response
from .serializers import *
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class AllClients(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]


class AllBook(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['room', 'passport_client']
    permission_classes = [IsAuthenticated]


class AllWorkers(generics.ListAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer
    permission_classes = [IsAuthenticated]

class AllBookWithInfoAboutRoomAndTypeRoom(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializerWithInfoAboutRoomAndTypeRoom

class CreateClient(generics.CreateAPIView, generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer
    permission_classes = [IsAuthenticated]

class GetCurrentWorker(APIView):
    def get(self, request, pk):
        worker = Workers.objects.filter(pk=pk)
        serializer = WorkersSerializer(worker, many=True)
        return Response({"Workers": serializer.data})


class CreateBook(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request):
        today = datetime.date(datetime.now())
        book = Book.objects.filter(data_end_living__lte=today)
        serializer = BookSerializerOnlyRoom(book, many=True)
        return Response({"Свободные номера на сегодня": serializer.data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        needed_books = Book.objects.filter(data_end_living__lte=self.request.data["data_start_living"])
        if len(needed_books) == 0:
            return Response("нет свободных мест на текущую дату", status=status.HTTP_400_BAD_REQUEST)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Бронирование создано", status=status.HTTP_201_CREATED)


class CreateWorker(generics.ListCreateAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkerCreateSerializer
    permission_classes = [IsAuthenticated]


class AllRooms(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type__count_places_in_room']


class UpdateWorker(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkerCreateSerializer
    permission_classes = [IsAuthenticated]


class DeleteCurrentBook(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializerWithInfoAboutRoomAndTypeRoom
    permission_classes = [IsAuthenticated]


class UpdateCurrentBook(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializerForUpdateStatusMove
    permission_classes = [IsAuthenticated]