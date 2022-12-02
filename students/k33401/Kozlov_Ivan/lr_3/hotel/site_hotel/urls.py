from django.urls import path
from .views import *

app_name = "site_hotel"

urlpatterns = [
    path('all_clients/', AllClients.as_view()),
    path('all_book/', AllBook.as_view()),
    path('all_workers/', AllWorkers.as_view()),
    path('all_books_with_room/', AllBookWithInfoAboutRoomAndTypeRoom.as_view()),
    path('create_client/', CreateClient.as_view()),
    path('get_worker/<int:pk>', GetCurrentWorker.as_view()),
    path('create_book/', CreateBook.as_view()),
    path('create_worker/', CreateWorker.as_view()),

]