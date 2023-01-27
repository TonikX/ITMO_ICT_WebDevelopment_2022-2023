from datetime import datetime

from rest_framework import serializers, generics
from rest_framework.response import Response

from library_app.models import *


# Специальный сериализатор для регистрации читателя работником библиотеки
class LibraryWorkerReaderUpdateSerializer(serializers.ModelSerializer):

    def update(self, instance, data):
        # меняем в БД дату регистрации в библиотеке, если номер читательского билета непуст
        instance.register_date = datetime.now().date() if data['library_card_number'] else None
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['library_card_number', 'reader_room', 'register_date']


class ReaderSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, data):
        # пишем в БД дату регистрации в библиотеке, если номер читательского билета непуст
        data['register_date'] = datetime.now().date() if data['library_card_number'] else None
        data['role'] = User.READER
        user = User.objects.create_user(**data)
        return user

    class Meta:
        model = User
        fields = ('username', 'password', 'phone', 'library_card_number', 'reader_room', 'register_date', 'education', 'is_have_degree')


class AuthorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, data):
        data['role'] = User.AUTHOR
        user = User.objects.create_user(**data)
        return user

    class Meta:
        model = User
        fields = ('username', 'password')


class ReadingRoomSerizalier(serializers.ModelSerializer):
    class Meta:
        model = ReadingRoom
        fields = '__all__'


class BookCopySerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(read_only=True, slug_field='title')
    reader = serializers.SlugRelatedField(read_only=True, slug_field='username')

    # StringRelatedField позволяет получить значение из метода модели __str__
    # в данном случае из модели ReadingRoom
    reading_rooms = serializers.StringRelatedField(many=True, source='reading_room')

    class Meta:
        model = BookCopy
        exclude = ['id', 'reading_room']


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['title', 'year', 'cypher']

    # Можно переопределить метод create способом ниже, если еще понадобиться создать экземпляр книги
    # def create(self, data):
    #     book = Book.objects.create(**data)
    #     book_copy = BookCopy.objects.create(book=book)
    #     request_data = self.context['request'].data
    #     book_copy.reading_room.set(request_data['reading_room'])
    #     return book


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['id', 'password', 'date_joined',
                   'surname', 'lastname', 'role',
                   'is_staff', 'is_active', 'last_login',
                   'is_superuser', 'groups', 'user_permissions',
                   'reader_room', 'education', 'first_name', 'last_name']
