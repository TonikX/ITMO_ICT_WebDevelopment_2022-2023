from rest_framework import serializers
from .models import *

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id','first_name','last_name','username']

class PassengerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['first_name','last_name','username','password']


class AirCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AirCompany
        fields = '__all__'

class PlaneSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Plane
        fields = '__all__'

class PlaneCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plane
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    plane = serializers.SlugRelatedField(read_only=True, slug_field='model')

    class Meta:
        model = Flight
        fields = '__all__'

class FlightCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()
    passenger = PassengerSerializer()

    class Meta:
        model = Ticket
        fields = '__all__'

class TicketCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'