# import serializers from the REST framework
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Airline, Passenger, Review, Air_travel
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# create a serializer class

class user_token (serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name')

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Airline_serializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'


class Passenger_serializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class Review_serializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class Air_travel_serializer(serializers.ModelSerializer):
    class Meta:
        model = Air_travel
        fields = '__all__'
