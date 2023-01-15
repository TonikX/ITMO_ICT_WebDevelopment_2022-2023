from django.urls import path, include

from .views import HotelViewSet, RoomTypeViewSet, RoomViewSet


urlpatterns = [
    path('account/', include('account_app.urls')),
    path('act/', include('reg_com_app.urls')),
    path('hotel/', HotelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('hotel/<int:pk>/', HotelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('hotel/room_type/<int:pk>/', RoomTypeViewSet.as_view({'get': 'retrieve', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('hotel/room_type/room/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
]
