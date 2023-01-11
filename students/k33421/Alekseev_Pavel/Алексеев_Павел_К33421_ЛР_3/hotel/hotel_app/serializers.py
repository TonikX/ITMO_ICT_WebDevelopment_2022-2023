from rest_framework import serializers

from .models import TypeRoom, Client, Room, Employee, Booking


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class TypeRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeRoom
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class BookSerializerWithInfoAboutRoomAndTypeRoom(serializers.ModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = Booking
        fields = "__all__"


class RoomCountSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ['count']

    def get_count(self, obj):
        return obj["count"]


class ClientCountSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['count']

    def get_count(self, obj):
        return obj["count"]

