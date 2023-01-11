from rest_framework import serializers

from .models import TypeRoom, Client, PriceConstructor, Room, Workers, Book


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class BookSerializerOnlyRoom(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["room"]

class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = "__all__"

class TypeRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeRoom
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    type = TypeRoomSerializer()
    class Meta:
        model = Room
        fields = "__all__"

class BookSerializerWithInfoAboutRoomAndTypeRoom(serializers.ModelSerializer):
    room = RoomSerializer()
    class Meta:
        model = Book
        fields = "__all__"


class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class WorkerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = "__all__"


class BookSerializerForUpdateStatusMove(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["status_move"]