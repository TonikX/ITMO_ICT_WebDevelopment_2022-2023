from django.contrib import admin
from django.urls import path
from hotel.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("guest/all", AllGuests.as_view()),
    path("guest/new", CreateGuest.as_view()),
    path("guest/<str:city>", GuestsByCity.as_view()),
    path("guest/<int:room_number>/<str:period_date_start>/<str:period_date_end>", GuestsByPeriod.as_view()),
    path("guests/<int:passport>/<str:period_date_start>/<str:period_date_end>", GuestsSamePeriods.as_view()),

    path("workers/all", AllWorkers.as_view()),
    path("workers/new", CreateWorker.as_view()),
    path("workers/<int:guest_passport>/<str:day_of_week>", GetWorkerByDayAndClient.as_view()),

    path("booking/all", AllBookings.as_view()),
    path("booking/new", CreateBooking.as_view()),

    #path("rooms/all", All.as_view()),
    path("rooms/free", FreeRoomsCount.as_view()),

    path("report/<int:quarter>", QReport.as_view()),

]
