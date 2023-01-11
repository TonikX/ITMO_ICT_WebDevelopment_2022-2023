from django.urls import path, include, re_path
from .views import *

app_name = "hotel_app"

urlpatterns = [

    path('all_clients/', AllClients.as_view()),
    path('create_client/', CreateClient.as_view()),
    path('client/<int:pk>/update', UpdateClient.as_view()),
    path('client/<int:pk>/delete', DeleteClient.as_view()),

    ###

    path('all_workers/', AllWorkers.as_view()),
    path('create_worker/', CreateWorker.as_view()),
    path('worker/<int:pk>/update', EmployeeUpdate.as_view()),
    path('worker/<int:pk>/delete', EmployeeDestroy.as_view()),

    ###

    path('room/', AllRooms.as_view()),
    path('create_room/', CreateRoom.as_view()),
    path('room/<int:pk>/update', RoomUpdate.as_view()),
    path('room/<int:pk>/delete', RoomUpdate.as_view()),

    ###

    path('all_book/', AllBook.as_view()),
    path('create_book/', CreateBook.as_view()),
    path('book/<int:pk>/update', UpdateBook.as_view()),
    path('book/<int:pk>/delete', DeleteBook.as_view()),

    ###

    path('all_books_with_room/', AllBookWithInfo.as_view()),
    path('count_of_room/', RoomCount.as_view()),
    path('count_of_client/', ClientCount.as_view()),


]
