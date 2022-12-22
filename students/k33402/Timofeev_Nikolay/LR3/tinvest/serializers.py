from . import models
from rest_framework import serializers
from djoser.serializers import UserSerializer as BaseUserSerializer


class MarketSerialize(serializers.HyperlinkedModelSerializer):
    group = serializers.CharField(source="get_group_display")
    label = serializers.CharField(source="get_label_display")

    class Meta:
        model = models.MarketEntry
        fields = [
            "id",
            "name",
            "description",
            "group",
            "label",
            "max_prices_last_month",
            "last_price",
        ]


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "username", "balance"]


class MarketRequestSerialize(serializers.HyperlinkedModelSerializer):
    seller_username = serializers.CharField(read_only=True, source="seller.username")
    asset_id = serializers.IntegerField(read_only=True, source="entry.id")

    class Meta:
        depth = 1
        model = models.MarketRequest
        fields = ["id", "seller_username", "asset_id", "count", "price", "total_price"]


class MarketRequestDealSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MarketRequestDeal
        fields = ["id", "buyer", "request"]


class MarketRequestSerializer(serializers.ModelSerializer):
    seller = serializers.ReadOnlyField(source="seller.username")

    class Meta:
        model = models.MarketRequest
        fields = ("id", "seller", "entry", "active", "count", "price", "ts_created")
        read_only_fields = ("id", "ts_created", "active")
