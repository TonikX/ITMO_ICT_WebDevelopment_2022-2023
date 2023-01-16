from django.contrib.auth import get_user_model
from django.db.models import Sum
from rest_framework import generics, authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from perfumery.models import Product
from perfumery.serializers import StaffSerializer, SaleRecordSerializer, ProductSerializer

User = get_user_model()


class StaffApiView(generics.ListAPIView):
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = User.objects.all()
	serializer_class = StaffSerializer


class ProductApiView(generics.ListAPIView):
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class SaleApiView(APIView):
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request):
		products = Product.objects.annotate(Sum("sales__quantity"))
		serializer = SaleRecordSerializer(products, many=True)
		return Response(serializer.data)
