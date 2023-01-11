from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

#просмотр информации о читателях
class ReaderListAPIView(ListAPIView):
   # permission_classes = [IsAuthenticated]
   serializer_class = ReaderSerializer
   queryset = Reader.objects.all()

#создание читателя
class CreateReader(CreateAPIView):
   #permission_classes = [IsAuthenticated]
   serializer_class = ReaderSerializer
   queryset = Reader.objects.all()
   
#просмотр всех произведений в бибилиотеке
class BookListAPIView(ListAPIView):
   #permission_classes = [IsAuthenticated]
   serializer_class = BookSerializer
   queryset = Book.objects.all()

#появление нового произведения в бибилиотеке
class CreateBook(CreateAPIView):
   #permission_classes = [IsAuthenticated]
   serializer_class = BookSerializer
   queryset = Book.objects.all()

#просмотр экземпляров произведений
class InstanceListAPIView(ListAPIView):
   #permission_classes = [IsAuthenticated]
   serializer_class = InstanceSerializer
   queryset = Instance.objects.all()

class CreateInstance(CreateAPIView):
   #permission_classes = [IsAuthenticated]
   serializer_class = InstanceSerializer
   queryset = Instance.objects.all()

   
#редактирование и удаление произведений
class OneBook(RetrieveUpdateDestroyAPIView):
   #permission_classes = [IsAuthenticated]
   serializer_class = BookSerializer
   queryset = Book.objects.all()


#редактирование и удаление экземпляров
class OneInstance(RetrieveUpdateDestroyAPIView):
   #permission_classes = [IsAuthenticated]
   serializer_class = InstanceSerializer
   queryset = Instance.objects.all()

   
#редактирование и удаление читателей
class OneReader(RetrieveUpdateDestroyAPIView):
   #permission_classes = [IsAuthenticated]
   serializer_class = ReaderSerializer
   queryset = Instance.objects.all()

   
#бронь книги
class BookInstance(CreateAPIView):
   serializer_class = ReaderBookSerializer 
   queryset = ReaderBook.objects.all()
   #permission_classes = [IsAuthenticated]

   def perform_create(self, serializer):
      serializer.save(librarian=self.request.user) 

#просмотр комнат
class RoomListAPIView(ListAPIView):
   serializer_class = RoomSerializer
   queryset = Room.objects.all()
   #permission_classes = [IsAuthenticated]

    
#создание комнат
class RoomCreateAPIView(CreateAPIView):
   serializer_class = RoomSerializer
   queryset = Room.objects.all()
   #permission_classes = [IsAuthenticated]


#редактирование и удаление комнат
class OneRoom(RetrieveUpdateDestroyAPIView):
   serializer_class = RoomSerializer
   queryset = Room.objects.all()
   #permission_classes = [IsAuthenticated]


#закрепление книги за комнатой
class RoomBook(CreateAPIView):
   serializer_class = BookRoomSerializer 
   queryset = BookRoom.objects.all()
   #permission_classes = [IsAuthenticated]

   def perform_create(self, serializer):
      serializer.save(librarian=self.request.user)

#закрепление читателя за комнатой
class RoomReader(CreateAPIView):
   serializer_class = ReaderRoomSerializer 
   queryset = ReaderRoom.objects.all()
   #permission_classes = [IsAuthenticated]

   def perform_create(self, serializer):
      serializer.save(librarian=self.request.user)