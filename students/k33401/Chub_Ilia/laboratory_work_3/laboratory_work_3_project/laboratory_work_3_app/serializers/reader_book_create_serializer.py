from rest_framework import serializers
from ..models import ReaderBookModel


class ReaderBookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaderBookModel
        fields = "__all__"
