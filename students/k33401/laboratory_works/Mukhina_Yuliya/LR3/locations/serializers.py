from rest_framework import serializers
from .models import City, Country, UserChoice


class CitySerializer(serializers.ModelSerializer):
    """Сериалайзер для городов"""
    class Meta:
        model = City
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    """Сериалайзер для стран"""
    class Meta:
        model = Country
        fields = '__all__'

    cities = CitySerializer(many=True)


class UserChoiceWriteSerializer(serializers.ModelSerializer):
    """Сериалайзер для выбранных городов (для записи)"""
    class Meta:
        model = UserChoice
        fields = '__all__'

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


class UserChoiceReadSerializer(serializers.ModelSerializer):
    """Сериалайзер для выбранных городов (для записи)"""
    class Meta:
        model = UserChoice
        fields = ['id', 'city']

    city = CitySerializer()
