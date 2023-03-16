from rest_framework import serializers
from .models import *

class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):

    room_type = PriceSerializer()

    class Meta:
        model = Room
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = "__all__"

class BookingAndClientSerializer(serializers.ModelSerializer):

    id_client = ClientSerializer()
    id_room = RoomSerializer()

    class Meta:
        model = Booking
        fields = "__all__"

class CleanerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cleaner
        fields = "__all__"

class ScheduleAndCleanerSerializer(serializers.ModelSerializer):

    id_cleaner = CleanerSerializer()

    day = serializers.CharField(source="get_day_display", read_only=True)

    class Meta:
        model = Schedule
        fields = "__all__"

class CleanerCreateSerializer(serializers.Serializer):
    last_name_cleaner = serializers.CharField(max_length=120)
    first_name_cleaner = serializers.CharField(max_length=120)
    patronymic_cleaner = serializers.CharField(max_length=120)

    def create(self, validated_data):
        cleaner = Cleaner(**validated_data)
        cleaner.save()
        return Cleaner(**validated_data)

class BookingCreateSerializer(serializers.Serializer):
    id_client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='passport')
    id_room = serializers.SlugRelatedField(queryset=Room.objects.all(), slug_field='id_room')
    date_start = serializers.DateField()
    date_end = serializers.DateField()

    def create(self, validated_data):
        booking = Booking(**validated_data)
        booking.save()
        return Booking(**validated_data)

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"

class ScheduleCreateSerializer(serializers.Serializer):
    id_cleaner = serializers.SlugRelatedField(queryset=Cleaner.objects.all(), slug_field='id_cleaner')
    id_floor = serializers.SlugRelatedField(queryset=Floor.objects.all(), slug_field='id_floor')
    day = serializers.CharField(max_length=3)

    def create(self, validated_data):
        schedule = Schedule(**validated_data)
        schedule.save()
        return Schedule(**validated_data)

class ScheduleSerializer(serializers.ModelSerializer):

    day = serializers.CharField(source="get_day_display", read_only=True)

    class Meta:
        model = Schedule
        fields = "__all__"