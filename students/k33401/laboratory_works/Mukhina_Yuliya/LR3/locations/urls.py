from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, CityViewSet, UserChoiceViewSet


router = DefaultRouter()
router.register('countries', CountryViewSet)
router.register('cities', CityViewSet)
router.register('choices', UserChoiceViewSet)


urlpatterns = [
    path('', include(router.urls))
]
