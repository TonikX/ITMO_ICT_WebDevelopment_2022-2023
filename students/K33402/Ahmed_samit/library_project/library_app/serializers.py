from rest_framework import serializers
from .models import *



class CopySerializer(serializers.ModelSerializer):
   class Meta:
     model = Copy
     fields = "__all__"
     



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

     
class BookInhallSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInHall
        fields = "__all__"
     
class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = "__all__"


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = "__all__"
        #exclude=('password', )

    def create(self, validated_data):
        user = Reader(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user  


class BookRetrieveSerializer(serializers.ModelSerializer):
    book_hall = HallSerializer(many=True)
    book_reader = ReaderSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"


class ReaderRetrieveSerializer(serializers.ModelSerializer):
    reader_hall = HallSerializer()
    reader_book = BookSerializer(many=True)

    class Meta:
        model = Reader
        fields = "__all__"    
        
        
        
class ReaderBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaderBook
        fields = "__all__"

    '''def create(self, validated_data):
        user = ReaderBook(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user'''
    
class ReaderBookRetrieveSerializer(serializers.ModelSerializer):
    reader_hall = HallSerializer()
    reader_book = BookSerializer(many=True)

    class Meta:
        model = ReaderBook
        fields = "__all__"