from rest_framework import serializers
from .models import *


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = "__all__"


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name", "patronymic", "email")


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    book_category = BookCategorySerializer()

    class Meta:
        model = Book
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = "__all__"


class AuthorshipListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authorship
        fields = "__all__"


class AuthorshipSerializer(serializers.ModelSerializer):
    author = AuthorListSerializer()
    book = BookSerializer()

    class Meta:
        model = Authorship
        fields = "__all__"


class EditionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = "__all__"


class EditionSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Edition
        fields = "__all__"
        depth = 1


class OrderManagerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderManager
        fields = "__all__"


class OrderManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderManager
        fields = "__all__"


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class BooksOrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksOrder
        fields = "__all__"


class BooksOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksOrder
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class OrderBookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBook
        fields = "__all__"


class OrderBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBook
        fields = "__all__"
