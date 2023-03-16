from rest_framework import serializers
from .models import *

class ReaderSerializer(serializers.ModelSerializer):
   books = serializers.SlugRelatedField(read_only=True, many=True, slug_field='books')

   class Meta:
     model = Reader
     fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
   class Meta:
     model = Book
     fields = "__all__"

  
class InstanceSerializer(serializers.ModelSerializer):
   class Meta:
     model = Instance
     fields = "__all__"


class ReaderBookSerializer(serializers.ModelSerializer):
   class Meta:
      model = ReaderBook
      fields = "__all__"

      
class RoomSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')
    
    class Meta:
       model = Room
       fields = "__all__"

       
class BookRoomSerializer(serializers.ModelSerializer):
   class Meta:
      model = BookRoom
      fields = "__all__"

class ReaderRoomSerializer(serializers.ModelSerializer):
   class Meta:
      model = ReaderRoom
      fields = "__all__"