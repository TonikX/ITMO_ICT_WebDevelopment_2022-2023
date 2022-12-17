from rest_framework import serializers

from hotel_app.models import Booking, Cleaning
from users_app.models import User


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "first_name", "middle_name", "last_name", "passport", "city")


class LivingClientsBookingSerializer(serializers.ModelSerializer):
    guest = GuestSerializer()

    class Meta:
        model = Booking
        fields = ("guest",)


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "first_name", "middle_name", "last_name", "passport")


class StaffByCleaningSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()

    class Meta:
        model = Cleaning
        fields = ("staff",)

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class GuestWithBookingSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True)

    class Meta:
        model = User
        fields = ("email", "first_name", "middle_name", "last_name", "passport", "city", "bookings")
