from rest_framework import serializers
from .models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = "__all__"


class CleanersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaners
        fields = "__all__"


class CleaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaning
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class RoomRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = "__all__"


class GuestRetrieveSerializer(serializers.ModelSerializer):
    # room_book = RoomSerializer(many=True)

    class Meta:
        model = Guest
        fields = "__all__"

class BookingRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"



class AvailableRoomSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display", read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'type', 'number', 'phone', 'price']