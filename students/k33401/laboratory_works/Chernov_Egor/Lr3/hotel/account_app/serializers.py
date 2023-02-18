from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Guest, Employee


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('phone_guest', 'passport_guest')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('hotel_empl', 'phone_employee', 'position_employee')
        depth = 1


class MyUserSerializer(serializers.ModelSerializer):
    user_guest = GuestSerializer(required=False)
    user_employee = EmployeeSerializer(required=False)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)

        try:
            instance.user_guest.phone_guest = validated_data.get('user_guest')['phone_guest'] \
                if validated_data.get('user_guest')['phone_guest'] else instance.user_guest.phone_guest
            instance.user_guest.passport_guest = validated_data.get('user_guest')['passport_guest'] \
                if validated_data.get('user_guest')['passport_guest'] else instance.user_guest.passport_guest
            instance.user_guest.save()
        except:
            instance.user_employee.phone_employee = validated_data.get('user_employee')['phone_employee'] \
                if validated_data.get('user_employee')['phone_employee'] else instance.user_employee.phone_employee
            instance.user_employee.position_employee = validated_data.get('user_employee')['position_employee'] \
                if validated_data.get('user_employee')['position_employee'] else instance.user_employee.position_employee
            instance.user_employee.save()

        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('id', 'is_staff', 'username', 'first_name', 'last_name', 'email', 'password', 'user_guest', 'user_employee')
