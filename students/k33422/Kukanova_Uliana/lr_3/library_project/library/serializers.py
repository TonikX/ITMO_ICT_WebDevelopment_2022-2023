from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    
  class Meta:
     model = Author
     fields = ["name"]

class PublisherSerializer(serializers.ModelSerializer):
    
  class Meta:
     model = Publisher
     fields = ["name"]

class RoomSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')
    
    class Meta:
     model = Room
     fields = "__all__"

class SectionSerializer(serializers.ModelSerializer):
    
  class Meta:
     model = Section
     fields = ["name"]


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()
    section = SectionSerializer()
    
    class Meta:
     model = Book
     fields = "__all__"

class BookAddSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = "__all__"

class ReaderSerializer(serializers.ModelSerializer):
   books = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')
   
   class Meta:
     model = Reader
     fields = "__all__"


class LibrarySerializer(serializers.ModelSerializer):
   room = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')
   
   class Meta:
     model = Library
     fields = "__all__"

