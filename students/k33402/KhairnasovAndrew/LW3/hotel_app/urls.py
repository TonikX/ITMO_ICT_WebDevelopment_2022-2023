from django.urls import path

from hotel_app.views import LivingClientsListView, ClientsFromCityView, GetCleaningStaffByClientAndWeekDay, \
    FreeRoomsCountView, GetClientsWithSamePeriod, QuartalReport, LivingClientsByRoomListView

urlpatterns = [
    path("livingClients/<str:fromDate>/<str:toDate>", LivingClientsListView.as_view()),
    path("livingClients/<int:roomId>/<str:fromDate>/<str:toDate>", LivingClientsByRoomListView.as_view()),
    path("clientsCountCity/<str:city>", ClientsFromCityView.as_view()),
    path("cleaningByCliendAndDay/<str:guestId>/<str:weekday>", GetCleaningStaffByClientAndWeekDay.as_view()),
    path("freeRooms/", FreeRoomsCountView.as_view()),
    path("clientsWithSamePerios/<int:guestId>/<str:fromDate>/<str:toDate>", GetClientsWithSamePeriod.as_view()),
    path("report/<int:q>", QuartalReport.as_view())
]
