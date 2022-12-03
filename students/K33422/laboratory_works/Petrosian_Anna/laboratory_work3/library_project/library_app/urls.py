from django.urls import path
from .views import *

app_name = "library_app"

urlpatterns = [
    path('books/', BookListAPIView.as_view()),  # list of books
    path('books/create/', BookCreateAPIView.as_view()),  # create book
    path('books/<int:pk>/', BookRetrieveAPIView.as_view()),  # book info by id

    # update / delete book by id
    path('books/edit/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view()),

    path('readers/', ReaderListAPIView.as_view()),  # list of readers
    path('readers/create/', ReaderCreateAPIView.as_view()),  # create reader
    path('readers/<int:pk>/', ReaderRetrieveAPIView.as_view()),  # reader info by id

    # update / delete reader by id
    path('readers/edit/<int:pk>/', ReaderRetrieveUpdateDestroyAPIView.as_view()),
    path('copies/', CopyListAPIView.as_view()), 
    path('copies/create/', CopyCreateAPIView.as_view()),
    #path('copies/<int:pk>/', CopyRetrieveAPIView.as_view()),  # book info by id
     path('bookinhall/create/', BookInhallCreateAPIView.as_view()), 
    #path('inst/<int:pk>/', OneICopy.as_view()),
    
    # path('report/', ReportApiView.as_view()),  # report
]