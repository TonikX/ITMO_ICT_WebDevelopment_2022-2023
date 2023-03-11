from rest_framework import serializers

from .models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class PlatfomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = Game
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    game = GameSerializer()
    platform = PlatfomSerializer()

    class Meta:
        model = Product
        fields = "__all__"


class ProductShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SellSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Sell
        fields = "__all__"


class UserOwnSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']
