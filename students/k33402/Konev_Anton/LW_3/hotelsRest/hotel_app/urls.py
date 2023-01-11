from django.urls import path
from hotel_app.views import LivingClients, ClientsByCity, GetCleaningStaffByClientAndDay, \
    FreeRoomsCount, GetClientsSamePeriods, QReport

urlpatterns = [
    path("living_clients/<int:room_id>/<str:from_date>/<str:to_date>", LivingClients.as_view()),
    path("clients_count_by_city/<str:city>", ClientsByCity.as_view()),
    path("cleaning_by_client_and_day/<int:guest_id>/<str:weekday>", GetCleaningStaffByClientAndDay.as_view()),
    path("free_rooms/", FreeRoomsCount.as_view()),
    path("clients_same_period/<int:guest_id>", GetClientsSamePeriods.as_view()),
    path("report/<int:q>", QReport.as_view())
]
