from rest_framework import serializers
from django.contrib.auth.models import User

from backend.api.app.serializers import UserSerialiser
from backend.profiles.models import Profile


class ProfileSer(serializers.ModelSerializer):
    """Сериализация профиля"""
    user = UserSerialiser()
    follow = UserSerialiser(many=True)
    class Meta:
        model = Profile
        fields = ('__all__')


class UserProfileSerialiser(serializers.ModelSerializer):
    """Сериализация пользователя по профилю"""
    profile = ProfileSer()
    class Meta:
        model = User
        fields = ("profile",)


class EditAvatar(serializers.ModelSerializer):
    """Редактирование автара"""
    class Meta:
        model = Profile
        fields = ("avatar", )
