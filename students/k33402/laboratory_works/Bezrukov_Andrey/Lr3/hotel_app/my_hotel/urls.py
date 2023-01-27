from django.urls import path, include
from rest_framework.routers import DefaultRouter

from my_hotel.views import RoomAPIView, GuestAPIView, StaffAPIView, CleaningAPIView, CheckinAPIView

router = DefaultRouter()
router.register(r'rooms', RoomAPIView)
router.register(r'guests', GuestAPIView)
router.register(r'staff', StaffAPIView)
router.register(r'cleaning', CleaningAPIView)
router.register(r'checkin', CheckinAPIView)


urlpatterns = [
    path('', include(router.urls))
]