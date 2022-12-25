from rest_framework import serializers
from .models import *


class RetrieveDriverUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class DriverOwnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ownership
        fields = "__all__"


class DriverLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverLicense
        fields = ("pk", "license_number", "type", "issue_date")


class DriverAndLicenseSerializer(serializers.ModelSerializer):
    driver_license = DriverLicenseSerializer(many=True, read_only=True)

    class Meta:
        model = Driver
        fields = ("pk", "username", "first_name", "last_name", "email", "birthday",
                  "passport", "address", "nationality", "driver_license")


class RetrieveDriverSerializer(serializers.ModelSerializer):
    driver_ownership = DriverOwnershipSerializer(many=True, read_only=True)
    driver_license = DriverLicenseSerializer(many=True, read_only=True)

    class Meta:
        model = Driver
        fields = ("pk", "username", "first_name", "last_name", "email", "birthday",
                  "passport", "address", "nationality", "driver_license", "driver_ownership")


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class CreateDriverSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Driver.objects.create(**validated_data)

    class Meta:
        model = Driver
        fields = "__all__"
