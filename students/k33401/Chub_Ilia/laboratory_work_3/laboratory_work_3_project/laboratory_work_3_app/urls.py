from django.urls import path
from .views import *

book_instances_urlpatterns = [
    path('book_instances/all', BookInstancesListView.as_view()),
    path('book_instances/create', BookInstancesCreateView.as_view()),
    path('book_instances/<str:pk>', BookInstancesGetUpdateDeleteView.as_view()),
    path('book_instances/free/by_book_id/<str:pk>', BookInstancesFreeByBookIdListView.as_view())
]

books_urlpatterns = [
    path('books/all', BookListView.as_view()),
    path('books/create', BookCreateView.as_view()),
    path('books/<str:pk>', BooksGetUpdateDeleteView.as_view())
]

readers_urlpatterns = [
    path('readers/all', ReadersListView.as_view()),
    path('readers/all/with_books', ReadersWithBooksListView.as_view()),
    path('readers/create', ReadersCreateView.as_view()),
    path('readers/<str:pk>', ReadersGetUpdateDeleteView.as_view())
]

user_reader_urlpatterns = [
    path('userreaders/create', UserReaderCreateView.as_view()),
    path('userreaders/<str:pk>', UserReaderGetUpdateDeleteView.as_view())
]

reader_books_urlpatterns = [
    path('readerbooks/create/', ReaderBooksCreateView.as_view()),
    path('readerbooks/by_reader/<str:pk>', ReaderBooksByReaderListView.as_view()),
    path('readerbooks/by_instance/<str:pk>', ReaderBooksByInstanceIdGetUpdateDeleteView.as_view())
]

urlpatterns = (
    []
    + book_instances_urlpatterns
    + books_urlpatterns
    + readers_urlpatterns
    + user_reader_urlpatterns
    + reader_books_urlpatterns
)
