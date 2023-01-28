from rest_framework import serializers
from .models import *


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "user_info", "img_url"]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["img_url", "user_info"]


class UsersEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEnrolledEvent
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class EventCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["text", "user", "event"]
