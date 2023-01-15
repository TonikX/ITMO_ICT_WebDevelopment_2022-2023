from django.urls import path

from .views import RegistrationViewSet, CommentViewSet


urlpatterns = [
    path('reg/', RegistrationViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('reg/<int:pk>/', RegistrationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('com/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('com/<int:pk>/', RegistrationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
