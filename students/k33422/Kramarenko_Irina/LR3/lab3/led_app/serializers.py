from rest_framework import serializers
from .models import Worker, Airplane, Flight


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = "__all__"


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"


class FlightPercentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['airport_start', 'airport_fin']


class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Flight
        fields = ['flight_number', 'number_seats']


class RepairAirplanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ['plane_number__count']


class WorkersNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['worker_id__count']


class AirplaneBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ['brand', 'plane_number__count']
