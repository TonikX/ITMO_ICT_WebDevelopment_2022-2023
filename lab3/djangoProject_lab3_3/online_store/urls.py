from django.urls import path
from .views import *


app_name = "online_store"


urlpatterns = [
    path('users/', UserAPIView.as_view()),
    path('products/<int:pk>',ProductAPIView.as_view()),
    path('add/product/',ProductCreateAPIView.as_view()),
    path('orders/',OrderAPIView.as_view()),
    path('add/toorder',AddPruductIntoOrder.as_view())

]