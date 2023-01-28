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
