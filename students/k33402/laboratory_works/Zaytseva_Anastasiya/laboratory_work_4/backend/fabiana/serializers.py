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


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = ("id", "product","quantity")


class OrderSerializer(serializers.ModelSerializer):
    cart = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ("id","cart")

    def get_cart(self, order_instance):
        query_datas = CartItem.objects.filter(order=order_instance)
        return [CartItemSerializer(cr).data for cr in query_datas]

