from rest_framework import serializers

from .models import Hotel, RoomType, Room


# Common
class CommonHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'name_hotel')


class CommonRoomTypeSerializer(serializers.ModelSerializer):
    type_rt = serializers.CharField(source='get_type_rt_display')

    class Meta:
        model = RoomType
        fields = ('id', 'type_rt', 'rating_rt', 'price_rt', 'des_rt')


# Hotel
class HotelSerializer(serializers.ModelSerializer):
    hotel_room_type = CommonRoomTypeSerializer(many=True)

    class Meta:
        model = Hotel
        fields = '__all__'


# RoomType
class RoomTypeRoomSerializer(serializers.ModelSerializer):
    status_room = serializers.CharField(source='get_status_room_display')

    class Meta:
        model = Room
        fields = ('id', 'number_room', 'status_room', 'review_room')


class RoomTypeSerializer(serializers.ModelSerializer):
    hotel_rt = CommonHotelSerializer()
    rt_room = RoomTypeRoomSerializer(many=True)
    type_rt = serializers.CharField(source='get_type_rt_display')

    class Meta:
        model = RoomType
        fields = '__all__'


# Room
class RoomSerializer(serializers.ModelSerializer):
    hotel_r = CommonHotelSerializer()
    rt_r = CommonRoomTypeSerializer()
    status_room = serializers.CharField(source='get_status_room_display')

    class Meta:
        model = Room
        fields = '__all__'
