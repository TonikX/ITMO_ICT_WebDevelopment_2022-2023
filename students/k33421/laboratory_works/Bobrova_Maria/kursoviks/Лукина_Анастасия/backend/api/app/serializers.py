from rest_framework import serializers
from django.contrib.auth.models import User

from backend.app.models import Exhibition


class UserSerialiser(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")


class ExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibition
        fields = "__all__"