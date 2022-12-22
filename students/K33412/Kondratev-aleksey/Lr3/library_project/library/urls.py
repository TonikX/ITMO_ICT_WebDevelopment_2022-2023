from django.urls import path
from .views import *

urlpatterns = [
    path('readers/list/', ReaderListAPIView.as_view()),
    path('readers/create/', CreateReader.as_view()),
    path('readers/<int:pk>/', OneReader.as_view()),
    path('books/list/', BookListAPIView.as_view()),
    path('books/create/', CreateBook.as_view()),
    path('books/<int:pk>/', OneBook.as_view()),
    path('inst/list/', InstanceListAPIView.as_view()),
    path('inst/create/', CreateInstance.as_view()),
    path('inst/<int:pk>/', OneInstance.as_view()),
    path('rooms/list/', RoomListAPIView.as_view()),
    path('rooms/create/', RoomCreateAPIView.as_view()),
    path('rooms/<int:pk>/', OneRoom.as_view()),
    path('book/readers/', BookReaders.as_view()),
    path('book/room/', RoomBook.as_view()),
    path('room/readers/', RoomReader.as_view()),
    path('book/inst/', BookInst.as_view()),
    path('readers/inst/<int:pk>', ReadersInst.as_view()),
    path('book/recently/', RecentlyBookDate.as_view()),
]