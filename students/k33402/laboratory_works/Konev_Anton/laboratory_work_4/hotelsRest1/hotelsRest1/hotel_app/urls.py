from django.urls import path
from .views import LivingClients, ClientsByCity, GetCleaningStaffByClientAndDay, \
    FreeRoomsList, GetClientsSamePeriods, QReport, RoomsAvailable, GuestBookingListCreate, GuestBookingUpdateDelete, \
    ApproveBookingView, CheckOutBookingNowView, RoomsAllView, RoomWithFreeTimeView, GuestsListView, GuestsGetView

urlpatterns = [
    path("living_clients/<int:room_id>/<str:from_date>/<str:to_date>", LivingClients.as_view()),
    path("clients_count_by_city/<str:city>", ClientsByCity.as_view()),
    path("cleaning_by_client_and_day/<int:guest_id>/<str:weekday>", GetCleaningStaffByClientAndDay.as_view()),
    path("free_rooms_list/", FreeRoomsList.as_view()),
    path("clients_same_period/<int:guest_id>", GetClientsSamePeriods.as_view()),
    path("report/<int:q>", QReport.as_view()),
    path("rooms/<str:start_ts>/<str:end_ts>", RoomsAvailable.as_view()),
    path("rooms/<str:start_ts>/<str:end_ts>/<str:room_type>", RoomsAvailable.as_view()),
    path("booking", GuestBookingListCreate.as_view()),
    path("booking/<int:pk>", GuestBookingUpdateDelete.as_view()),
    path("approve_booking/<int:pk>", ApproveBookingView.as_view()),
    path("check_out_booking/<int:pk>", CheckOutBookingNowView.as_view()),
    path("all_rooms/", RoomsAllView.as_view()),
    path("rooms_with_time/", RoomWithFreeTimeView.as_view()),
    path("guests/", GuestsListView.as_view()),
    path("guests/<int:pk>", GuestsGetView.as_view()),
]
