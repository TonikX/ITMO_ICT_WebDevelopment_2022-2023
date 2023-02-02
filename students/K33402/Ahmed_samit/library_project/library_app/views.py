from django.db.models import Sum

from .serializers import *
from rest_framework.generics import *


class CopyListAPIView(ListAPIView):
    serializer_class = CopySerializer
    queryset = Copy.objects.all()

class CopyCreateAPIView(CreateAPIView):
    serializer_class = CopySerializer
    queryset = Copy.objects.all()


class CopykRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CopySerializer
    queryset = Copy.objects.all()

class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
#class CopyRetrieveAPIView(RetrieveAPIView):
    #serializer_class = CopyRetrieveSerializer
    #queryset = Copy.objects.all()

class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()



class BookCreateAPIView(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookRetrieveAPIView(RetrieveAPIView):
    serializer_class = BookRetrieveSerializer
    queryset = Book.objects.all()


class ReaderListAPIView(ListAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class ReaderCreateAPIView(CreateAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class ReaderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class ReaderRetrieveAPIView(RetrieveAPIView):
    serializer_class = ReaderRetrieveSerializer
    queryset = Reader.objects.all() 

class BookInhallrListAPIView(ListAPIView):
    serializer_class = BookInhallSerializer
    queryset = BookInHall.objects.all()

class BookInhallCreateAPIView(CreateAPIView):
    serializer_class = BookInhallSerializer
    queryset = BookInHall.objects.all()
    
class BookInhallRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookInhallSerializer
    queryset = BookInHall.objects.all()


class HallrListAPIView(ListAPIView):
    serializer_class = HallSerializer
    queryset = Hall.objects.all()
    
class HallCreateAPIView(CreateAPIView):
    serializer_class = HallSerializer
    queryset = Hall.objects.all()
    
class HallRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HallSerializer
    queryset = Hall.objects.all()



class ReaderBookListAPIView(ListAPIView):
    serializer_class = ReaderBookSerializer
    queryset = ReaderBook.objects.all()


class ReaderBookCreateAPIView(CreateAPIView):
    serializer_class = ReaderBookSerializer
    queryset = ReaderBook.objects.all()


class ReaderBookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderBookSerializer
    queryset = ReaderBook.objects.all()


class ReaderRetrieveAPIView(RetrieveAPIView):
    serializer_class = ReaderRetrieveSerializer
    queryset = Reader.objects.all()