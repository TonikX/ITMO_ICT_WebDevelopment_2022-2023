from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Registration, Comment
from hotel_app.models import Hotel, RoomType, Room


# Common
class RegComUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class RegComHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'name_hotel')


class RegComRoomTypeSerializer(serializers.ModelSerializer):
    type_rt = serializers.CharField(source='get_type_rt_display', read_only=True)

    class Meta:
        model = RoomType
        fields = ('id', 'type_rt', 'price_rt')


# Registration
class RegistrationRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'number_room')


class RegistrationSerializer(serializers.ModelSerializer):
    user_reg = RegComUserSerializer(read_only=True)
    hotel_reg = RegComHotelSerializer(read_only=True)
    rt_reg = RegComRoomTypeSerializer(read_only=True)
    room_reg = RegistrationRoomSerializer(read_only=True)
    status_reg_reg = serializers.CharField(source='get_status_reg_reg_display')
    status_pay_reg = serializers.CharField(source='get_status_pay_reg_display')

    class Meta:
        model = Registration
        fields = '__all__'


# Comment
class CommentRoomSerializer(serializers.ModelSerializer):
    hotel_r = RegComHotelSerializer(read_only=True)
    rt_r = RegComRoomTypeSerializer(read_only=True)
    status_room = serializers.CharField(source='get_status_room_display')

    class Meta:
        model = Room
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user_com = RegComUserSerializer(read_only=True)
    room_com = CommentRoomSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
