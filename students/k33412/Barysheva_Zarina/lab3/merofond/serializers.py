from rest_framework import serializers
from .models import *
from djoser.serializers import UserSerializer


class MeroUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ["id", "username"]

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'title', 'address']

class EventTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventType
        fields = ['id', 'title']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'organizer', 'title', 'description', 'location', 'datetime', 'event_type']

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'user', 'event']