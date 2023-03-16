from django.urls import path
from .views import *


urlpatterns = [
    path('clients/', Clients.as_view()),
    # path('rooms/', Rooms.as_view()),
    path('vacant/', RoomsVacant.as_view()),
    path('cleaners/', Cleaners.as_view()),
    # path('cleaner/create/', CleanerCreateView.as_view()),
    path('bookings/', Bookings.as_view()),
    path('schedules/', Schedules.as_view()),
    # path('schedules/day/', SchedulesByDay.as_view()),
    path('cleaners/<pk>', CleanerDeleteView.as_view()),
    path('bookings/<pk>', BookingUpdateView.as_view()),
    path('schedules/<pk>', ScheduleUpdateView.as_view()),
]