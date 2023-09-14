# Лабораторная работа 3

## Структура проекта

- `LR3` - основная директория проекта
- `tinvest` - приложение

## Настройки

- `LR3/settings.py`  

_Настройки авторизации_

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework.authentication.TokenAuthentication",),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
}
AUTH_USER_MODEL = "tinvest.User"
DJOSER = {
    "SERIALIZERS": {"current_user": "tinvest.serializers.UserSerializer"},
}
```

_Установленные приложения_

```python
INSTALLED_APPS = [
    "djoser",
    "corsheaders",
    "tinvest",
    "rest_framework",
    "rest_framework.authtoken",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_yasg",
]
```

- `LR3/urls.py`  

_URL-паттерны приложения + Swagger/Redoc_

```python
schema_view = get_schema_view(
   openapi.Info(
      title="TInvest REST API",
      default_version='v1',
      description="Timofeev Invest Documentation",
      contact=openapi.Contact(email="timofeevnik41@gmail.com"),
      license=openapi.License(name="Apache 2 Licensed"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", include("tinvest.urls")),
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

## Приложение tinvest

- Исходный код URL-паттернов `urls.py`

```python
from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"market", views.MarketViewSet)
router.register(r"users", views.UsersViewSet)
router.register(r"market-requests", views.MarketRequestCreateView)
router.register(r"transactions", views.MarketRequestDealViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("assets/", views.get_user_assets)
]
```

- Исходный код моделей `models.py`
 
```python
from __future__ import annotations
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(null=True)
    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=255)

    @property
    def balance(self):
        balance, _ = UserBalance.objects.get_or_create(user=self)
        return balance.balance

    @property
    def owned_assets(self):
        assets = {}
        for e in MarketEntry.objects.all():
            bought = sum([
                d.request.count
                for d in MarketRequestDeal.objects.filter(
                    buyer=self,
                    request__entry=e,
                ).all()
            ])
            sold = sum([
                d.request.count 
                for d in MarketRequestDeal.objects.filter(
                    request__seller=self,
                    request__entry_id=e,
                ).all()
            ])
            amount = max(bought - sold, 0)
            if amount != 0:
                assets[e.id] = {'amount' : max(bought - sold, 0), 'meta': str(e)} # type: ignore
        return assets

    def __str__(self) -> str:
        return self.username


class UserBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f"{self.user}: {self.balance}"


class MarketableGroup(models.TextChoices):
    CRYPTO = ("CR", "Cryptocurrency")
    STOCKS = ("ST", "Stock")
    CURRENCY = ("CU", "Currency")


class MarketableLabel(models.TextChoices):
    SELECTED = ("SL", "Editor's choice")
    RAPID = ("RP", "Rapid Growth")
    POPULAR = ("PP", "Popular")
    NEW = ("NW", "Recently listed")


class MarketEntry(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)
    group = models.CharField(max_length=2, choices=MarketableGroup.choices)
    label = models.CharField(max_length=2, choices=MarketableLabel.choices)

    @property
    def last_price(self) -> float:
        deal = MarketRequestDeal.objects.filter(request__entry=self).last()
        if deal:
            return float(deal.request.price)
        return 0.0

    @property
    def max_prices_last_month(self):
        from django.utils import timezone
        from django.db.models import Max
        from django.db.models.functions import TruncDate

        now = timezone.now()

        request_deals = MarketRequestDeal.objects.filter(
            request__entry=self, ts_created__gte=now - timezone.timedelta(days=30)
        )

        prices = (
            request_deals.annotate(date=TruncDate("ts_created"))
            .values("date")
            .annotate(max_total_price=Max("request__price"))
        )

        return prices

    def __str__(self) -> str:
        return self.name


class OfferType(models.TextChoices):
    sell = ('s', 'Sell')
    buy = ('b', 'Buy')


class MarketOffer(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    entry = models.ForeignKey(MarketEntry, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    type = models.CharField(max_length=2, choices=OfferType.choices, default=OfferType.buy)
    count = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ts_created = models.DateTimeField(auto_now=True, editable=True)

    @property
    def total_price(self):
        return self.count * self.price

    def __str__(self) -> str:
        return f"({self.entry}) {self.seller} - {self.total_price}"


class MarketRequestDeal(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.ForeignKey(MarketOffer, on_delete=models.CASCADE)
    ts_created = models.DateTimeField(default=timezone.now, editable=True)

    def __str__(self) -> str:
        return f"{self.buyer}:{self.request}"
```

- Исходный код сериализаторов `serializers.py`

```python
from . import models
from rest_framework import serializers
from djoser.serializers import UserSerializer as BaseUserSerializer


class MarketSerialize(serializers.HyperlinkedModelSerializer):
    group = serializers.CharField(source="get_group_display")
    label = serializers.CharField(source="get_label_display")

    class Meta:
        model = models.MarketEntry
        fields = [
            "id",
            "name",
            "description",
            "group",
            "label",
            "max_prices_last_month",
            "last_price"
        ]


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name = 'UserSerializerOverriden'
        fields = ["id", "username", "balance"]


class MarketRequestSerialize(serializers.HyperlinkedModelSerializer):
    seller_username = serializers.CharField(read_only=True, source="seller.username")
    asset_id = serializers.IntegerField(read_only=True, source="entry.id")

    class Meta:
        depth = 1
        model = models.MarketOffer
        fields = ["id", "seller_username", "asset_id", "count", "price", "total_price"]


class MarketRequestDealSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MarketRequestDeal
        fields = ["id", "buyer", "request"]
        read_only_fields = ("id", "buyer")


class MarketRequestSerializer(serializers.ModelSerializer):
    seller = serializers.ReadOnlyField(source="seller.username")
    my_request = serializers.SerializerMethodField()
    type_offer = serializers.ReadOnlyField(source='get_type_display')

    class Meta:
        model = models.MarketOffer
        fields = ("id", "seller", "entry", "type", "type_offer", "my_request", "active", "count", "price", "ts_created")
        read_only_fields = ("id", "my_request", "type_offer", "ts_created", "active")

    def get_my_request(self, obj):
        request = self.context.get("request")
        if request and request.user:
            return obj.seller == request.user
        return False
```

- Исходный код views:

```python
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
```