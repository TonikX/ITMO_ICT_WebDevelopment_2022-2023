from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Product

User = get_user_model()


class StaffSerializer(serializers.ModelSerializer):
	full_name = serializers.SerializerMethodField()

	class Meta:
		model = User
		fields = ["id", "full_name", "position", "working_days", "working_hours"]

	def get_full_name(self, user: User):
		return f"{user.first_name} {user.last_name}"


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = "__all__"


class SaleRecordSerializer(serializers.ModelSerializer):
	sales__quantity__sum = serializers.IntegerField()

	class Meta:
		model = Product
		fields = ["id",
		          "image_name",
		          "name",
		          "price",
		          "quantity",
		          "sales__quantity__sum"]
