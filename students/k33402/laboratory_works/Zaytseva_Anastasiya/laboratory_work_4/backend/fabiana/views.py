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
    queryset = FabianaUser.objects.all()

class FabianaUserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = FabianaUserSerializer
    queryset = FabianaUser.objects.all()

class CartItemListAPIView(generics.ListAPIView):
    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user,purchased=False)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response({"cart_items": serializer.data})

class CartItemDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

class OrderListAPIView(generics.ListAPIView):
    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response({"orders": serializer.data})

class CartItemCreateAPIView(views.APIView):
    def post(self, request):
        product = request.data.get("product")
        quantity = request.data.get("quantity")

        item = CartItem.objects.create(product_id=product,quantity=quantity,user_id=request.user.id)
        cart = CartItem.objects.filter(user_id=request.user.id,purchased=False)
        item.save()

        return Response({"Success": "Cart item {} created succesfully.".format(item.id)})

class OrderCreateAPIView(views.APIView):
    def post(self, request):
        cart = CartItem.objects.filter(user=request.user,purchased=False)
        order = Order(user=request.user)
        order.save()
        cart.update(purchased=True,order=order)

        return Response({"Success": "Order {} created succesfully.".format(order.id)})
