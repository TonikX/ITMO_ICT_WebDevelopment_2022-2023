from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView

from .serializers import *


# Просмотр списков

class ReaderListAPIView(ListAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class BookListAPIView(ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class InstanceListAPIView(ListAPIView):
    serializer_class = InstanceSerializer
    queryset = InstanceBook.objects.all()


class HallListAPIView(ListAPIView):
    serializer_class = HallSerializer
    queryset = Hall.objects.all()


# Создание записей
class CreateReader(CreateAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class CreateBook(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class CreateInstance(CreateAPIView):
    serializer_class = InstanceSerializer
    queryset = InstanceBook.objects.all()


# Редактирование и удаление записей
class ChangeBookOnHands(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = BooksOnHandsSerializer
    queryset = BooksOnHands.objects.all()


class ChangeInstancePlace(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = InstancePlaceSerializer
    queryset = InstancePlace.objects.all()
    # who take book


class ChangeReaderHall(RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderHallSerializer
    queryset = ReaderHall.objects.all()


class ChangeBook(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class ChangeInstance(RetrieveUpdateDestroyAPIView):
    serializer_class = InstanceSerializer
    queryset = InstanceBook.objects.all()


class ChangeReader(RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


# Закрепление кого-то за чем-то
class CreateBookOnHand(CreateAPIView):
    serializer_class = BooksOnHandsSerializer
    queryset = BooksOnHands.objects.all()

    # def perform_create(self, serializer):
    #    serializer.save(librarian=self.request.user)


class CreateInstancePlace(CreateAPIView):
    serializer_class = InstancePlaceSerializer
    queryset = InstancePlace.objects.all()

    # permission_classes = [IsAuthenticated]
    #
    # def perform_create(self, serializer):
    #     serializer.save(librarian=self.request.user)


class CreateHallReader(CreateAPIView):
    serializer_class = ReaderHallSerializer
    queryset = ReaderHall.objects.all()



class ReaderRetrieveAPIView(RetrieveAPIView):
    serializer_class = ReaderRetrieveSerializer
    queryset = Reader.objects.all()