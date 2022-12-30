from django.urls import path
from .views import *
urlpatterns = [
    path('readers/list/', ReaderListAPIView.as_view()),
    path('readers/<int:pk>/', ReaderRetrieveAPIView.as_view()),  # reader info by id

    path('books/list/', BookListAPIView.as_view()),

    path('instances/list/',  InstanceListAPIView.as_view()),
    path('instances/<int:pk>/',  InstanceRetrieveAPIView.as_view()),

    path('halls/list/', HallListAPIView.as_view()),

    path('reader_books/list/', BookOnHandsListAPIView.as_view()),
    path('reader_books/<int:pk>/', BookOnHandsRetrieveAPIView.as_view()),

    # path('readers/create/',  CreateReader.as_view()),
    # path('books/create/',  CreateBook.as_view()),
    # path('instance/create/',  CreateInstance.as_view()),
    #
    # path('instance_place/create/', CreateInstancePlace.as_view()),
    # path('reader_place/create/', CreateHallReader.as_view()),
    path('reader_books/create/',  CreateBookOnHand.as_view()),
    path('return/<int:pk>/', BookOnHandsRetrieveUpdateDestroyAPIView.as_view()),
    #
    # path('booking/<int:pk>/update/', ChangeBookOnHands.as_view()),
    # path('reader_place/<int:pk>/update/', ChangeReaderHall.as_view()),
    # path('instance_place/<int:pk>/update/', ChangeInstancePlace.as_view()),
    #
    # path('book/<int:pk>/update/', ChangeBook.as_view()),
    # path('instance/<int:pk>/update/', ChangeInstance.as_view()),
    # path('reader/<int:pk>/update/', ChangeReader.as_view()),

]