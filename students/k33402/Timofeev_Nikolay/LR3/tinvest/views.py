from . import models, serializers
from rest_framework import viewsets, permissions, status, renderers
from rest_framework.response import Response
from django.http import Http404


class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class MarketViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = models.MarketEntry.objects.all()
    serializer_class = serializers.MarketSerialize

    def get_queryset(self):
        queryset = models.MarketEntry.objects.all()
        if (filter_ := self.request.query_params.get("search")) is not None:  # type: ignore
            queryset = queryset.filter(name__iregex=filter_)
        return queryset
    


class MarketRequestViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = models.MarketRequest.objects.all()
    serializer_class = serializers.MarketRequestSerialize
    renderer_classes = [renderers.JSONRenderer]

    def get_queryset(self):
        queryset = models.MarketRequest.objects.all()
        if (entry_id := self.request.query_params.get("entry")) is not None:  # type: ignore
            queryset = queryset.filter(entry__id=entry_id)
        return queryset


class MarketRequestDealViewSet(viewsets.ModelViewSet):
    """Model for viewing and creating orders"""

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = models.MarketRequestDeal.objects.all()
    serializer_class = serializers.MarketRequestDealSerialize


class MarketRequestCreateView(viewsets.ModelViewSet):
    """View for creating new market order for current user"""

    permission_classes = [permissions.IsAuthenticated]
    queryset = models.MarketRequest.objects.all()
    serializer_class = serializers.MarketRequestSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        serializer: serializers.MarketRequestSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(seller=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
