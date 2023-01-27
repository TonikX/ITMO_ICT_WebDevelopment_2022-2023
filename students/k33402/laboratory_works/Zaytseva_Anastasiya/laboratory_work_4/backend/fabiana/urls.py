from django.urls import path
from .views import *

urlpatterns = [
    path('products', ProductListAPIView.as_view()),
    path('products/<int:pk>', ProductRetrieveAPIView.as_view()),
    path('product_count', ProductCountAPIView.as_view()),
    path('orders', OrderListAPIView.as_view()),
    path('orders/create', OrderCreateAPIView.as_view()),
    path('cart-items', CartItemListAPIView.as_view()),
    path('cart-items/create', CartItemCreateAPIView.as_view()),
    path('cart-items/<int:pk>/remove', CartItemDestroyAPIView.as_view()),
    path('users/<int:pk>', FabianaUserRetrieveAPIView.as_view()),
]