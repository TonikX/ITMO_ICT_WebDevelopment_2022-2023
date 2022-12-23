from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class FabianaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FabianaUser
        fields = "__all__"