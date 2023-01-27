from rest_framework import serializers
from .models import *


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserOnEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersEvents
        fields = "__all__"

class UserEventsSerializer(serializers.ModelSerializer):
    event_id = EventSerializer()
    class Meta:
        model = UsersEvents
        fields = ("id", "event_id")