from django.urls import path, include
from rest_framework.routers import DefaultRouter

from library.views import (
    BooksViewsSet,
    StorageBooksViewSet,
    LibraryViewSet,
    ReaderViewSet,
    LibrarianViewSet,
    ReadTicketViewSet
)

router = DefaultRouter()
router.register('books', BooksViewsSet)
router.register('books/locations', StorageBooksViewSet)
router.register(r'library', LibraryViewSet)
router.register(r'readers', ReaderViewSet)
router.register(r'librarians', LibrarianViewSet)
router.register(r'tickets', ReadTicketViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
