from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import *
from .models import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

class BookCategoryListAPIView(generics.ListAPIView):
    serializer_class = BookCategorySerializer
    queryset = BookCategory.objects.all()

class BookCategoryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BookCategorySerializer
    queryset = BookCategory.objects.all()

class BookCategoryUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BookCategorySerializer
    queryset = BookCategory.objects.all()

class BookCategoryDestroyAPIView(generics.DestroyAPIView):
    serializer_class = BookCategorySerializer
    queryset = BookCategory.objects.all()

class AuthorListAPIView(generics.ListAPIView):
    serializer_class = AuthorListSerializer
    queryset = Author.objects.all()

class AuthorRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class AuthorUpdateAPIView(generics.UpdateAPIView):
    serializer_class = AuthorListSerializer
    queryset = Author.objects.all()

class AuthorDestroyAPIView(generics.DestroyAPIView):
    serializer_class = AuthorListSerializer
    queryset = Author.objects.all()

class BookListAPIView(generics.ListAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()

class BookRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()

class BookDestroyAPIView(generics.DestroyAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()

class AuthorshipListAPIView(generics.ListAPIView):
    serializer_class = AuthorshipListSerializer
    queryset = Authorship.objects.all()

class AuthorshipRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = AuthorshipSerializer
    queryset = Authorship.objects.all()

class AuthorshipUpdateAPIView(generics.UpdateAPIView):
    serializer_class = AuthorshipListSerializer
    queryset = Authorship.objects.all()

class AuthorshipDestroyAPIView(generics.DestroyAPIView):
    serializer_class = AuthorshipListSerializer
    queryset = Authorship.objects.all()

class EditionListAPIView(generics.ListAPIView):
    serializer_class = EditionListSerializer
    queryset = Edition.objects.all()

class EditionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = EditionSerializer
    queryset = Edition.objects.all()

class EditionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = EditionListSerializer
    queryset = Edition.objects.all()

class EditionDestroyAPIView(generics.DestroyAPIView):
    serializer_class = EditionListSerializer
    queryset = Edition.objects.all()

class OrderManagerListAPIView(generics.ListAPIView):
    serializer_class = OrderManagerListSerializer
    queryset = OrderManager.objects.all()

class OrderManagerRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = OrderManagerSerializer
    queryset = OrderManager.objects.all()

class OrderManagerUpdateAPIView(generics.UpdateAPIView):
    serializer_class = OrderManagerListSerializer
    queryset = OrderManager.objects.all()

class OrderManagerDestroyAPIView(generics.DestroyAPIView):
    serializer_class = OrderManagerListSerializer
    queryset = OrderManager.objects.all()

class CustomerListAPIView(generics.ListAPIView):
    serializer_class = CustomerListSerializer
    queryset = Customer.objects.all()

class CustomerRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class CustomerUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CustomerListSerializer
    queryset = Customer.objects.all()

class CustomerDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CustomerListSerializer
    queryset = Customer.objects.all()

class BooksOrderListAPIView(generics.ListAPIView):
    serializer_class = BooksOrderListSerializer
    queryset = BooksOrder.objects.all()

class BooksOrderRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BooksOrderSerializer
    queryset = BooksOrder.objects.all()

class BooksOrderUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BooksOrderListSerializer
    queryset = BooksOrder.objects.all()

class BooksOrderDestroyAPIView(generics.DestroyAPIView):
    serializer_class = BooksOrderListSerializer
    queryset = BooksOrder.objects.all()

class OrderBookListAPIView(generics.ListAPIView):
    serializer_class = OrderBookListSerializer
    queryset = OrderBook.objects.all()

class OrderBookRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = OrderBookSerializer
    queryset = OrderBook.objects.all()

class OrderBookUpdateAPIView(generics.UpdateAPIView):
    serializer_class = OrderBookListSerializer
    queryset = OrderBook.objects.all()

class OrderBookDestroyAPIView(generics.DestroyAPIView):
    serializer_class = OrderBookListSerializer
    queryset = OrderBook.objects.all()

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v2',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="az20022002@icloud.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)






















