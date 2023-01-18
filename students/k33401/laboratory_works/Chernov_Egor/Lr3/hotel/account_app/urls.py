from django.urls import path

from .views import UserViewSet


urlpatterns = [
    path('user/', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('user/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
