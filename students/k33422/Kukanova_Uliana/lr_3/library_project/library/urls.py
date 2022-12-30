from django.urls import path
from .views import *

app_name = "library"


urlpatterns = [
    path('readers/list/', ReaderListAPIView.as_view()),
    path('books/list/', BookListAPIView.as_view()),
    path('library/list/', LibraryListAPIView.as_view()),
    path('rooms/list/', RoomListAPIView.as_view()),
    path('readers/<int:pk>/', SingleReader.as_view()),
    path('books/<int:pk>/', SingleBook.as_view()),
    path('library/<int:pk>/', SingleLibrary.as_view()),
    path('rooms/<int:pk>/', SingleRoom.as_view()),
    path('books/create/', BookCreateAPIView.as_view()),
    path('readers/create/', ReaderCreateAPIView.as_view()),
    path('rooms/create/', RoomCreateAPIView.as_view())
]