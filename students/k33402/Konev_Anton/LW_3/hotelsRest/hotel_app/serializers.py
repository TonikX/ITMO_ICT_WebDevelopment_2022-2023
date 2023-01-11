from rest_framework import serializers

from hotel_app.models import Booking, Cleaning, Guest, CleaningStaff


class CountObj:
    def __init__(self, count):
        self.count = count


class CountSerializer(serializers.Serializer):
    count = serializers.IntegerField()


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ("first_name", "middle_name", "last_name", "passport", "city")


class LivingClientsBookingSerializer(serializers.ModelSerializer):
    guest = GuestSerializer()

    class Meta:
        model = Booking
        fields = ("guest",)


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleaningStaff
        fields = ("first_name", "middle_name", "last_name")


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
        model = Guest
        fields = ("first_name", "middle_name", "last_name", "passport", "city", "bookings")
