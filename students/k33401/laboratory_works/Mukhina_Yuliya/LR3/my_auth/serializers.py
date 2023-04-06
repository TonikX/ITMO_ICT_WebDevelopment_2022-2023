from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from locations.models import City, UserChoice


class RegistrationSerializer(UserCreateSerializer):
    """Сериалайзер для регистрации с заданием города"""
    class Meta(UserCreateSerializer.Meta):
        fields = ['username', 'first_name', 'last_name', 'password', 'city']

    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all(), write_only=True)

    def validate(self, attrs):
        # Не пердаем в родительский validate() атрибут city, чтобы не было бага
        attrs_without_city = attrs.copy()
        attrs_without_city.pop('city')
        super(RegistrationSerializer, self).validate(attrs_without_city)
        return attrs

    def create(self, validated_data):
        city = validated_data.pop('city')
        print(validated_data)
        created_user = super(RegistrationSerializer, self).create(validated_data)
        # Создаем для пользователя выбранный город
        UserChoice.objects.create(city=city, user=created_user)
        return created_user
