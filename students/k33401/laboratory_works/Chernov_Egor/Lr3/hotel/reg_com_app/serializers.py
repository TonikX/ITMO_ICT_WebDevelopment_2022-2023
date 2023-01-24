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
    type_rt = serializers.CharField(source='get_type_rt_display')

    class Meta:
        model = RoomType
        fields = ('id', 'type_rt', 'price_rt')


# Registration
class RegistrationRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'number_room')


class RegistrationSerializer(serializers.ModelSerializer):
    user_reg = RegComUserSerializer()
    hotel_reg = RegComHotelSerializer()
    rt_reg = RegComRoomTypeSerializer()
    room_reg = RegistrationRoomSerializer()
    status_reg_reg = serializers.CharField(source='get_status_reg_reg_display')
    status_pay_reg = serializers.CharField(source='get_status_pay_reg_display')

    class Meta:
        model = Registration
        fields = '__all__'


class WriteRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


# Comment
class CommentRoomSerializer(serializers.ModelSerializer):
    hotel_r = RegComHotelSerializer()
    rt_r = RegComRoomTypeSerializer()
    status_room = serializers.CharField(source='get_status_room_display')

    class Meta:
        model = Room
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user_com = RegComUserSerializer()
    room_com = CommentRoomSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class WriteCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
