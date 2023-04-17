from rest_framework import serializers
from .models import *


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = "__all__"


class TransitLandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransitLanding
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"


class FlightShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'numbers']


class FullFlightSerializer(serializers.ModelSerializer):
    plane = PlaneSerializer(read_only=True)
    transit_land = TransitLandingSerializer(many=True, read_only=True)
    employee = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Flight
        fields = ['id', 'numbers', 'distance', 'air_departure', 'air_arrival', 'dep_dt', 'arr_dt', 'plane',
                  'transit_land', 'employee']


class FullEmployeeSerializer(serializers.ModelSerializer):
    flight = FlightShortSerializer(read_only=True, many=True)

    class Meta:
        model = Employee
        fields = ['full_name', 'age', 'position', 'education', 'experience', 'passport', 'flight']


class FullPlaneSerializer(serializers.ModelSerializer):
    flight = FlightShortSerializer(read_only=True, many=True)

    class Meta:
        model = Plane
        fields = ['number', 'type', 'num_seats', 'speed', 'company', 'flight']

