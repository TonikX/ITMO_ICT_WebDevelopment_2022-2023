from rest_framework import serializers
from .models import *

class ReaderSerializer(serializers.ModelSerializer):
   # books_on_hands = serializers.SlugRelatedField(read_only=True,
   #                                      many=True,
   #                                      slug_field='books')

   class Meta:
     model = Reader
     fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
   class Meta:
     model = Book
     fields = "__all__"

class InstanceSerializer(serializers.ModelSerializer):
   book = BookSerializer()
   class Meta:
     model = InstanceBook
     fields = "__all__"

class HallSerializer(serializers.ModelSerializer):
    # books = serializers.SlugRelatedField(read_only=True,
    #                                      many=True,
    #                                      slug_field='books')

    class Meta:
       model = Hall
       fields = "__all__"

# class BookOnHandsSer(serializers.ModelSerializer):
#     class Meta:
#         model = BooksOnHands
#         fields = "__all__"

class BooksOnHandsSerializer(serializers.ModelSerializer):
   reader = ReaderSerializer()
   instance = InstanceSerializer()
   class Meta:
      model = BooksOnHands
      fields = "__all__"

class BookOnHandsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksOnHands
        fields = "__all__"


class InstancePlaceSerializer(serializers.ModelSerializer):
   class Meta:
      model = InstancePlace
      fields = "__all__"

class ReaderHallSerializer(serializers.ModelSerializer):
   class Meta:
      model = ReaderHall
      fields = "__all__"



class ReaderRetrieveSerializer(serializers.ModelSerializer):
    reader_hall = HallSerializer()
    instances_on_hands = InstanceSerializer(many=True)

    class Meta:
        model = Reader
        fields = "__all__"

class InstanceRetrieveSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    who_reads = ReaderSerializer(many=True)
    instance_hall = HallSerializer()
    class Meta:
        model = InstanceBook
        fields = "__all__"