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
            "last_price"
        ]


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name = 'UserSerializerOverriden'
        fields = ["id", "username", "balance"]


class MarketRequestSerialize(serializers.HyperlinkedModelSerializer):
    seller_username = serializers.CharField(read_only=True, source="seller.username")
    asset_id = serializers.IntegerField(read_only=True, source="entry.id")

    class Meta:
        depth = 1
        model = models.MarketOffer
        fields = ["id", "seller_username", "asset_id", "count", "price", "total_price"]


class MarketRequestDealSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MarketRequestDeal
        fields = ["id", "buyer", "request"]
        read_only_fields = ("id", "buyer")


class MarketRequestSerializer(serializers.ModelSerializer):
    seller = serializers.ReadOnlyField(source="seller.username")
    my_request = serializers.SerializerMethodField()
    type_offer = serializers.ReadOnlyField(source='get_type_display')

    class Meta:
        model = models.MarketOffer
        fields = ("id", "seller", "entry", "type", "type_offer", "my_request", "active", "count", "price", "ts_created")
        read_only_fields = ("id", "my_request", "type_offer", "ts_created", "active")

    def get_my_request(self, obj):
        request = self.context.get("request")
        if request and request.user:
            return obj.seller == request.user
        return False
