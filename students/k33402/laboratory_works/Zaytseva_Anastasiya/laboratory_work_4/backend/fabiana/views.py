from django.shortcuts import render
from rest_framework import views, generics, permissions
from .serializers import *
from .models import *
from django.db.models import Count
from rest_framework.response import Response

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        limit = self.request.query_params.get('limit')
        color = self.request.query_params.get('color')
        if color is not None:
            queryset = Product.objects.filter(color=color)
        if limit is not None:
            limit = int(limit)
            queryset = queryset[:limit]
        return queryset

class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductCountAPIView(views.APIView):
   def get(self, request):
       count = Product.objects.count()
       return Response({"product_count": count})

class FabianaUserListAPIView(generics.ListAPIView):
    serializer_class = FabianaUserSerializer
    queryset = Product.objects.all()

class FabianaUserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = FabianaUserSerializer
    queryset = Product.objects.all()
