from django.db.models.query import QuerySet
from django.shortcuts import render
from django.utils import timezone
from .models import *
from .serializers import *
from datetime import datetime, timedelta
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework import generics
from rest_framework.views import APIView, Response
from datetime import date


class ReaderListAPIView(ListAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class CreateReader(CreateAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class CreateBook(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class InstanceListAPIView(ListAPIView):
    serializer_class = InstanceSerializer
    queryset = Instance.objects.all()


class CreateInstance(CreateAPIView):
    serializer_class = InstanceSerializer
    queryset = Instance.objects.all()


class OneBook(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class OneInstance(RetrieveUpdateDestroyAPIView):
    serializer_class = InstanceSerializer
    queryset = Instance.objects.all()


class OneReader(RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderSerializer
    queryset = Instance.objects.all()


class BookReaders(CreateAPIView):
    serializer_class = ReaderBookSerializer
    queryset = ReaderBook.objects.all()


class RoomListAPIView(ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomCreateAPIView(CreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class OneRoom(RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomBook(CreateAPIView):
    serializer_class = BookRoomSerializer
    queryset = BookRoom.objects.all()



class RoomReader(CreateAPIView):
    serializer_class = ReaderRoomSerializer
    queryset = ReaderRoom.objects.all()


class BookInst(CreateAPIView):
    serializer_class = BookInstSerializer
    queryset = BookInst.objects.all()


class ReadersInst(generics.RetrieveAPIView):
    serializer_class = ReaderInstsSerializer
    queryset = Reader.objects.all()

class RecentlyBookDate(ListAPIView):
    # serializer_class = RecentlyBookDateSerializer
    # queryset = ReaderBook.objects.all()


    def get(self, request):
        today = date.today()
        reader = ReaderBook.objects.filter(date__lte=today)
        content = {"reader": reader}
        return Response(content)


