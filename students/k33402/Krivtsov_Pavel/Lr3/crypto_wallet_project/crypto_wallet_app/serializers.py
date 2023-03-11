from rest_framework import serializers
from .models import Currency, Ownership, Transaction, Discussion, Tag, User, Comment


class DiscussionUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username"]


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = "__all__"


class OwnershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ownership
        fields = "__all__"


class OwnershipUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ownership
        fields = ["count"]


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"


class DiscussionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discussion
        fields = "__all__"


class DiscussionExtInfoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    user = DiscussionUserSerializer()

    class Meta:
        model = Discussion
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
