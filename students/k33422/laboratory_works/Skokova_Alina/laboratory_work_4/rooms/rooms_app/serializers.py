from rest_framework import serializers
from .models import *


# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = "__all__"


class PriceSerializer(serializers.ModelSerializer):

    room_type = serializers.CharField(source="get_room_type_display", read_only=True)

    class Meta:
        model = Price
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):

    room_type = PriceSerializer()

    class Meta:
        model = Room
        fields = "__all__"


class CleanerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cleaner
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):

    id_client = ClientSerializer()
    id_room = RoomSerializer()

    class Meta:
        model = Booking
        fields = "__all__"


class BookingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):

    id_cleaner = CleanerSerializer()

    day = serializers.CharField(source="get_day_display", read_only=True)

    class Meta:
        model = Schedule
        fields = "__all__"


class ScheduleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = "__all__"