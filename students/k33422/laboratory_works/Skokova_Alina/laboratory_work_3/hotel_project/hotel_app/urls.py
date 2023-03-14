from django.urls import path
from .views import *


app_name = "hotel_app"


urlpatterns = [
    path('clients/<id_room>/<date_start>/<date_end>', BookingRoomDatesListAPIView.as_view()),
    path('clients/<city>', ClientListAPIView.as_view()),
    path('client/<passport>', BookingAndClientListAPIView.as_view()),
    path('cleaner/<id_room>/<day>', CleanerGetAPIView.as_view()),
    path('vacant/', RoomVacantListAPIView.as_view()),
    path('clients/<date_start>/<date_end>', BookingDatesListAPIView.as_view()),
    path('cleaner-create/', CleanerCreateView.as_view()),
    path('cleaner-delete/<pk>', CleanerDeleteView.as_view()),
    path('booking-update/<pk>', BookingUpdateView.as_view()),
    path('booking-create/', BookingCreateView.as_view()),
    path('schedule-create/', ScheduleCreateView.as_view()),
    path('schedule-update/<pk>', ScheduleGetView.as_view()),
    path('schedule/<id_cleaner>', CleanerAndScheduleListAPIView.as_view()),
    path('floor/<id_floor>', RoomsPerFloor.as_view()),
]