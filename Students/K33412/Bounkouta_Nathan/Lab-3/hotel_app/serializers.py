from rest_framework import serializers
from .models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class RoomRetrieveSerializer(serializers.ModelSerializer):
    client_room = ClientSerializer(many=True)

    class Meta:
        model = Room
        fields = "__all__"


class ClientRetrieveSerializer(serializers.ModelSerializer):
    room_client = RoomSerializer(many=True)

    class Meta:
        model = Client
        fields = "__all__"