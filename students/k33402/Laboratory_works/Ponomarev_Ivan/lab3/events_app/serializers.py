from rest_framework import serializers
from .models import *
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id','email', 'first_name', 'last_name', 'username', 'password', 'phone','user_image' )
class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone', 'user_image']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    place = LocationSerializer()
    participants = MyUserSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = '__all__'


class UserEventEnrollmentSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    class Meta:
        model = UserEventEnrollment
        fields = '__all__'

class UserEventEnrollmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEventEnrollment
        fields='__all__'