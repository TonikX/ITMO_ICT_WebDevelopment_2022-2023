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
