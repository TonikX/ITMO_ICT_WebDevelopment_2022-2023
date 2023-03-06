from rest_framework import viewsets, permissions

from library.models import (
    Book,
    BookStorageLocation,
    Library,
    Reader,
    Librarian,
    ReaderTicket
)
from library.serializers import (
    BookSerializer,
    BookStorageLocationSerializer,
    LibrarySerializer,
    ReaderSerializer,
    LibrarianSerializer,
    ReaderTicketSerializer
)


class BooksViewsSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class StorageBooksViewSet(viewsets.ModelViewSet):
    queryset = BookStorageLocation.objects.all()
    serializer_class = BookStorageLocationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class LibrarianViewSet(viewsets.ModelViewSet):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ReadTicketViewSet(viewsets.ModelViewSet):
    queryset = ReaderTicket.objects.all()
    serializer_class = ReaderTicketSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
