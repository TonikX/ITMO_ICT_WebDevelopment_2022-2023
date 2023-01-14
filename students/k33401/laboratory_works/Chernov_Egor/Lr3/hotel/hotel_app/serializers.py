from rest_framework import serializers

from .models import Hotel, RoomType, Room


# Hotel
class HotelRoomTypeSerializer(serializers.ModelSerializer):
    type_rt = serializers.CharField(source='get_type_rt_display')

    class Meta:
        model = RoomType
        fields = ('pk', 'type_rt', 'rating_rt', 'price_rt', 'des_rt')


class HotelSerializer(serializers.ModelSerializer):
    hotel_room_type = HotelRoomTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = '__all__'


# RoomType
class RoomRoomTypeSerializer(serializers.ModelSerializer):
    status_room = serializers.CharField(source='get_status_room_display')

    class Meta:
        model = Room
        fields = ('id', 'number_room', 'status_room', 'review_room')


class RoomTypeSerializer(serializers.ModelSerializer):
    rt_room = RoomRoomTypeSerializer(many=True, read_only=True)
    type_rt = serializers.CharField(source='get_type_rt_display', read_only=True)

    class Meta:
        model = RoomType
        fields = '__all__'


# Room
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
