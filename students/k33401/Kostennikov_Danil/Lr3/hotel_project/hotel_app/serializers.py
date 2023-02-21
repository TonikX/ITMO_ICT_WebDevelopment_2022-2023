from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "firstName", "lastName")


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class CleaningSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Cleening
        fields = "__all__"


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    type = RoomTypeSerializer()

    class Meta:
        model = Room
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class BookingFieldRoomSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Booking
        fields = "__all__"


class BookingRoomSerializer(serializers.ModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = Booking
        fields = "__all__"


class CountSerializer(serializers.Serializer):
    count = serializers.IntegerField()
