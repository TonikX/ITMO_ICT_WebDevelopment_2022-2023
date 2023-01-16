from . import models, serializers
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
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


class BalanceMixin:
    def _reduce_balance(self, user, amount):
        assert user.balance is not None # ensure balance
        balance = models.UserBalance.objects.filter(user=user).first()
        if not balance:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        balance.balance -= float(amount)
        balance.save()


class MarketRequestCreateView(viewsets.ModelViewSet, BalanceMixin):
    """View for creating new market order for current user"""

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = models.MarketOffer.objects.all()
    serializer_class = serializers.MarketRequestSerializer

    def get_serializer_context(self):
        return {"request": self.request}

    def get_queryset(self):
        queryset = models.MarketOffer.objects.filter(active=True).all()
        if (entry_id := self.request.query_params.get("entry")) is not None:  # type: ignore
            queryset = queryset.filter(entry__id=entry_id)
        return queryset

    def destroy(self, request, *args, **kwargs):
        try:
            instance: models.MarketOffer = self.get_object()
            if not instance or instance.seller.id != request.user.id: # type: ignore
                return Response(status=status.HTTP_403_FORBIDDEN)
            if not instance.active:
                return Response(status=status.HTTP_409_CONFLICT)
            instance.active = False
            instance.save() 
            self._reduce_balance(request.user, -instance.total_price)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        serializer: serializers.MarketRequestSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        total = (int(request.data.get('price', 1)) * int(request.data.get('count', 1)))
        if request.data.get('type') == 'b':
            # if buy request
            if self.request.user.balance < total: # type: ignore
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
            serializer.save(seller=self.request.user)
            self._reduce_balance(request.user, total)
        elif request.data.get('type') == 's':
            # if sell request
            if assets := self.request.user.owned_assets:  # type: ignore
                if assets.get(int(request.data.get('entry')))['amount'] < int(request.data.get('count')):
                    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
            serializer.save(seller=self.request.user)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        try:
            instance: models.MarketOffer = self.get_object()
            if self.request.user.balance < instance.total_price:  # type: ignore
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
            deal = models.MarketRequestDeal.objects.create(
                buyer=request.user,
                request=instance,
            )
            if instance.type == models.OfferType.sell:
                self._reduce_balance(instance.seller, -instance.total_price)
            self._reduce_balance(request.user, instance.total_price)
            instance.active = False
            instance.save()
            deal.save()
        except Http404:
            pass
        return Response()


class MarketRequestDealViewSet(viewsets.ModelViewSet, BalanceMixin):
    """View working with market order deal for current user"""

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = models.MarketRequestDeal.objects.all()
    serializer_class = serializers.MarketRequestDealSerialize

    def create(self, request, *args, **kwargs):
        serializer: serializers.MarketRequestDealSerialize = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
        instance = models.MarketOffer.objects.filter(id=serializer.data.get('request', {}).get("id", -1)).first()
        if not instance:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if self.request.user.balance < instance.total_price:  # type: ignore
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer.save(seller=self.request.user)
        self._reduce_balance(request.user, instance.total_price)  
        instance.active = False
        instance.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)    


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_assets(request) -> Response:
    return Response({"message": f"@{request.user} assets", "assets": request.user.owned_assets})
