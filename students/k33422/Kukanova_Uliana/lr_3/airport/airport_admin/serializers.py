from rest_framework import serializers
from .models import *


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['passport', 'full_name', 'age', 'education', 'experience', 'in_crew']


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightAsScheduled
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class AirlineAdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirlineAdministration
        fields = '__all__'


class TransitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transit
        fields = '__all__'
