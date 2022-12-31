from rest_framework import serializers
from .models import *


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = "__all__"

class CreateGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = "__all__"

class CreateWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = "__all__"

class CreateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('room_number', 'guest', 'date_start', 'date_end')


class CountObj:
    def __init__(self, count):
        self.count = count

class CountSerializer(serializers.Serializer):
    count = serializers.IntegerField()


class BookSerializerOnlyRoom(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["room_number"]

class GuestsByPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["guest"]

class CleaningSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cleaning
        fields = ['id_worker']

