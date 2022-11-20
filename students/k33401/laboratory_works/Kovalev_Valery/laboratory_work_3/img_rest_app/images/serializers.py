from abc import ABC

from rest_framework import serializers
from images.models import *


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class LikePhotoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = LikePhoto
        fields = "__all__"


class CollectionPhotoSerializerExpanded(serializers.ModelSerializer):
    photo = PhotoSerializer(many=False)

    class Meta:
        model = CollectionPhoto
        fields = "__all__"


class CollectionPhotoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, data):
        if self.context["request"].user != data["collection"].user:
            raise serializers.ValidationError("Access to the collection is prohibited")
        return data

    class Meta:
        model = CollectionPhoto
        fields = "__all__"


class KeywordsSerializer(serializers.Serializer):
    keyword = serializers.CharField()
    total = serializers.IntegerField()


class CollectionSerializerExpanded(serializers.ModelSerializer):
    photos = CollectionPhotoSerializerExpanded(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = ["title", "photos"]


class CollectionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Collection
        fields = "__all__"
