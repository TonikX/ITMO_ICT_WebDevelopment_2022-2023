from rest_framework import serializers
from ..models import ReaderModel


class ReaderWithBookSerializer(serializers.ModelSerializer):
    books_instances = serializers.SlugRelatedField(read_only=True, many=True, slug_field='id')

    class Meta:
        model = ReaderModel
        fields = "__all__"
