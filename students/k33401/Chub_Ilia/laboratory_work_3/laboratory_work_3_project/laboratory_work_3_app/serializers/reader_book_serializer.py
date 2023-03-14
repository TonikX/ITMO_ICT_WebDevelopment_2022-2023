from rest_framework import serializers
from ..models import ReaderBookModel


class ReaderBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaderBookModel
        fields = "__all__"
        depth = 2
