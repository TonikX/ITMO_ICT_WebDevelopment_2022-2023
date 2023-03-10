from rest_framework import serializers
from django.contrib.auth import get_user_model

from library.models import (
    Book,
    BookStorageLocation,
    Library,
    Librarian,
    ReaderTicket,
    Reader,
    BookReader
)
from djoser.serializers import UserSerializer as BaseUserSerializer

User = get_user_model()


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name = 'UserSerializerOverriden'
        fields = ["id", "username", "first_name", "last_name"]


class BookSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()

    def get_location(self, book: Book) -> dict:
        location = BookStorageLocation.objects.filter(book=book)
        serialized_data = BookStorageLocationSerializer(location).data
        return serialized_data

    class Meta:
        model = Book
        fields = [
            'name', 'author', 'publish_date', 'translator',
            'publishment_office', 'original_language',
            'knowledge_area', 'location'
        ]


class BookStorageLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStorageLocation
        fields = '__all__'


class LibrarySerializer(serializers.ModelSerializer):
    librarians = serializers.SerializerMethodField()
    reader_tickets = serializers.SerializerMethodField()

    def get_librarians(self, library: Library) -> dict:
        librarians = Librarian.objects.filter(library=library)
        serialized_data = LibrarianSerializer(librarians, many=True).data
        return serialized_data

    def get_reader_tickets(self, library: Library) -> dict:
        reader_tickets = ReaderTicket.objects.filter(library=library)
        serialized_data = ReaderTicketSerializer(reader_tickets, many=True).data
        return serialized_data

    class Meta:
        model = Library
        fields = ['name', 'librarians', 'reader_tickets']


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'


class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'


class ReaderTicketSerializer(serializers.ModelSerializer):
    books_history = serializers.SerializerMethodField()

    def get_books_history(self, ticket: ReaderTicket) -> dict:
        books = BookReader.objects.filter(reader=ticket).values('book')
        serialized_data = BookSerializer(books, many=True).data
        return serialized_data

    class Meta:
        model = ReaderTicket
        fields = [
            'owner', 'registration_date',
            'expiration_date', 'books_history'
        ]


class ReaderBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReader
        fields = '__all__'
