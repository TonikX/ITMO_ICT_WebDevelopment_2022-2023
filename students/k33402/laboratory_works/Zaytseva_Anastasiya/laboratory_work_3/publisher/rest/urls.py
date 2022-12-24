from django.urls import path
from .views import *

urlpatterns = [
    path('book-category', BookCategoryListAPIView.as_view()),
    path('book-category/<int:pk>', BookCategoryRetrieveAPIView.as_view()),
    path('book-category/<int:pk>/remove', BookCategoryDestroyAPIView.as_view()),
    path('book-category/<int:pk>/edit', BookCategoryUpdateAPIView.as_view()),

    path('author', AuthorListAPIView.as_view()),
    path('author/<int:pk>', AuthorRetrieveAPIView.as_view()),
    path('author/<int:pk>/remove', AuthorDestroyAPIView.as_view()),
    path('author/<int:pk>/edit', AuthorUpdateAPIView.as_view()),

    path('book', BookListAPIView.as_view()),
    path('book/<int:pk>', BookRetrieveAPIView.as_view()),
    path('book/<int:pk>/remove', BookDestroyAPIView.as_view()),
    path('book/<int:pk>/edit', BookUpdateAPIView.as_view()),

    path('authorship', AuthorshipListAPIView.as_view()),
    path('authorship/<int:pk>', AuthorshipRetrieveAPIView.as_view()),
    path('authorship/<int:pk>/remove', AuthorshipDestroyAPIView.as_view()),
    path('authorship/<int:pk>/edit', AuthorshipUpdateAPIView.as_view()),

    path('edition', EditionListAPIView.as_view()),
    path('edition/<int:pk>', EditionRetrieveAPIView.as_view()),
    path('edition/<int:pk>/remove', EditionDestroyAPIView.as_view()),
    path('edition/<int:pk>/edit', EditionUpdateAPIView.as_view()),

    path('order-manager', OrderManagerListAPIView.as_view()),
    path('order-manager/<int:pk>', OrderManagerRetrieveAPIView.as_view()),
    path('order-manager/<int:pk>/remove', OrderManagerDestroyAPIView.as_view()),
    path('order-manager/<int:pk>/edit', OrderManagerUpdateAPIView.as_view()),

    path('customer', CustomerListAPIView.as_view()),
    path('customer/<int:pk>', CustomerRetrieveAPIView.as_view()),
    path('customer/<int:pk>/remove', CustomerDestroyAPIView.as_view()),
    path('customer/<int:pk>/edit', CustomerUpdateAPIView.as_view()),

    path('books-order', BooksOrderListAPIView.as_view()),
    path('books-order/<int:pk>', BooksOrderRetrieveAPIView.as_view()),
    path('books-order/<int:pk>/remove', BooksOrderDestroyAPIView.as_view()),
    path('books-order/<int:pk>/edit', BooksOrderUpdateAPIView.as_view()),

    path('order-book', OrderBookListAPIView.as_view()),
    path('order-book/<int:pk>', OrderBookRetrieveAPIView.as_view()),
    path('order-book/<int:pk>/remove', OrderBookDestroyAPIView.as_view()),
    path('order-book/<int:pk>/edit', OrderBookUpdateAPIView.as_view()),

    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]