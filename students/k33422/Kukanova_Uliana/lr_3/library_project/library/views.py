from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

class ReaderListAPIView(generics.ListAPIView):
   serializer_class = ReaderSerializer
   queryset = Reader.objects.all()

class ReaderCreateAPIView(generics.CreateAPIView):
   serializer_class = ReaderSerializer
   queryset = Reader.objects.all()

class BookListAPIView(generics.ListAPIView):
   serializer_class = BookSerializer
   queryset = Book.objects.all()

class BookCreateAPIView(generics.CreateAPIView):
   serializer_class = BookAddSerializer
   queryset = Book.objects.all()

class LibraryListAPIView(generics.ListAPIView):
   serializer_class = LibrarySerializer
   queryset = Library.objects.all()

class RoomListAPIView(generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class RoomCreateAPIView(generics.CreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class SingleReader(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = ReaderSerializer
   queryset = Reader.objects.all()

class SingleBook(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = BookSerializer
   queryset = Book.objects.all()

class SingleLibrary(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = LibrarySerializer
   queryset = Library.objects.all()

class SingleRoom(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = RoomSerializer
   queryset = Room.objects.all()


"""class EditWarrior(generics.RetrieveUpdateDestroyAPIView):
   serializer_class = WarriorSerializer
   queryset = Warrior.objects.all()"""
