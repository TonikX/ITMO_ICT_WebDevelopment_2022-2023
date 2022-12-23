from django.urls import path
from .views import *

urlpatterns = [
    path('products', ProductListAPIView.as_view()),
    path('products/<int:pk>', ProductRetrieveAPIView.as_view()),
    path('product_count', ProductCountAPIView.as_view()),
    path('users', FabianaUserListAPIView.as_view()),
    path('users/<int:pk>', FabianaUserRetrieveAPIView.as_view()),
]