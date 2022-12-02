from django.shortcuts import render
from rest_framework.views import APIView
from .models import TypeRoom, Client, PriceConstructor, Room, Workers, Book
from rest_framework import serializers, generics, status
from rest_framework.response import Response
from .serializers import *
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class AllClients(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = (TokenAuthentication,)


class AllBook(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = (TokenAuthentication,)


class AllWorkers(generics.ListAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer
    authentication_classes = (TokenAuthentication,)

class AllBookWithInfoAboutRoomAndTypeRoom(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializerWithInfoAboutRoomAndTypeRoom

class CreateClient(generics.CreateAPIView, generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer

class GetCurrentWorker(APIView):
    def get(self, request, pk):
        worker = Workers.objects.filter(pk=pk)
        serializer = WorkersSerializer(worker, many=True)
        return Response({"Workers": serializer.data})


class CreateBook(generics.CreateAPIView):
    serializer_class = BookSerializer
    authentication_classes = (TokenAuthentication,)
    def get(self, request):
        today = datetime.date(datetime.now())
        book = Book.objects.filter(data_end_living__lte=today)
        serializer = BookSerializerOnlyRoom(book, many=True)
        return Response({"Свободные номера на сегодня": serializer.data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        needed_books = Book.objects.filter(data_end_living__lte=self.request.data["data_start_living"])
        all_rooms = Room.objects.all()
        current_room = request.data["room"]
        if len(needed_books) == 0:
            return Response("нет свободных мест на текущую дату", status=status.HTTP_400_BAD_REQUEST)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Бронирование создано", status=status.HTTP_201_CREATED)


class CreateWorker(generics.CreateAPIView, generics.ListAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkerCreateSerializer
