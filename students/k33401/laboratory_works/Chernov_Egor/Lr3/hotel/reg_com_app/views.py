from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import Registration, Comment
from .serializers import RegistrationSerializer, WriteRegistrationSerializer, CommentSerializer, WriteCommentSerializer
from .permisions import IsOwner


class RegistrationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | IsOwner, ]
    queryset = Registration.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_staff:
    #         return Registration.objects.all()
    #     return Registration.objects.filter(user_reg=user)

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return WriteRegistrationSerializer
        return RegistrationSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.permission_classes = [AllowAny, ]
        elif self.action in ('create', 'update', 'destroy'):
            self.permission_classes = [IsAdminUser | IsOwner, ]
        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return WriteCommentSerializer
        return CommentSerializer
