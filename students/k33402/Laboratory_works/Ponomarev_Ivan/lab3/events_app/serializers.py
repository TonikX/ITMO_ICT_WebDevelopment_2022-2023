from rest_framework import serializers
from .models import *


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number']


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
    place = LocationSerializer

    class Meta:
        model = Event
        fields = '__all__'


class UserEventEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEventEnrollment
        fields = '__all__'
