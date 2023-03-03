from django.urls import path
from .views import *

app_name = "library"

urlpatterns = [
    path('books/', BookListAPIView.as_view()),
    path('books/<int:pk>/', BookAPIView.as_view()),

    # admin permissions required
    path('books/<int:pk>/delete/', BookDeleteAPIView.as_view()),
    path('books/<int:pk>/update/', BookUpdateAPIView.as_view()),
    path('books/create/', BookCreateAPIView.as_view()),

    path('genres/', GenreListAPIView.as_view()),
    path('genres/<int:pk>/', GenreAPIView.as_view()),

    path('authors/', AuthorListAPIView.as_view()),
    path('authors/<int:pk>/', AuthorAPIView.as_view()),

    path('reading/<int:book>/add/', ReadingCreateAPIView.as_view()),
    path('reading/<int:book>/update/', ReadingUpdateAPIView.as_view()),

    path('me/', UserAPIView.as_view())
]
