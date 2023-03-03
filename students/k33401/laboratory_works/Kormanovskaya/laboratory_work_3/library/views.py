import django.contrib.auth.models
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *


class BookListAPIView(generics.ListAPIView):
    """
    Show book list with detailed information.
    """
    serializer_class = BookFullSerializer
    queryset = Book.objects.all()


class BookAPIView(generics.RetrieveAPIView):
    """
    Book information by 'id'.
    """
    serializer_class = BookFullSerializer
    queryset = Book.objects.all()


class BookUpdateAPIView(generics.UpdateAPIView):
    """
    Book update by 'id'.
    """
    permission_classes = [IsAdminUser]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDeleteAPIView(generics.DestroyAPIView):
    """
    Book destroy by 'id'.
    """
    permission_classes = [IsAdminUser]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookCreateAPIView(generics.CreateAPIView):
    """
    Create new book.
    """
    permission_classes = [IsAdminUser]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class GenreListAPIView(generics.ListAPIView):
    """
    Show genres list.
    """
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class AuthorListAPIView(generics.ListAPIView):
    """
    Show authors list
    """
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class GenreAPIView(generics.RetrieveAPIView):
    """
    Show book list of selected genre.
    """
    serializer_class = GenreBookSerializer
    queryset = Genre.objects.all()


class AuthorAPIView(generics.RetrieveAPIView):
    """
    Show book list writen by selected author.
    """
    serializer_class = AuthorBookSerializer
    queryset = Author.objects.all()


class UserAPIView(APIView):
    """
    User info
    """

    def get(self, request):
        try:
            user = User.objects.filter(username=request.user)
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data[0])
        except:
            return Response()


class ReadingCreateAPIView(generics.CreateAPIView):
    serializer_class = ReadingCreateUpdateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['book'] = self.kwargs['book']
        return context


class ReadingUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ReadingCreateUpdateSerializer

    def get_object(self):
        book = self.kwargs['book']
        user = self.request.user.id
        return Reading.objects.get(book_id=book, user_id=user)
