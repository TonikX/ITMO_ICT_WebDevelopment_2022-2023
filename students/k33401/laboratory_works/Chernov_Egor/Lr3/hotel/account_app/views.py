from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from django.contrib.auth.models import User
from .serializers import UserSerializer
from .permissions import IsOwner


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser | IsOwner, ]
