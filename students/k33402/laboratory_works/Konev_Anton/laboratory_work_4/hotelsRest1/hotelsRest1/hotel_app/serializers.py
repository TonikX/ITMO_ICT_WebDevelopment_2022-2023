import datetime
from collections import OrderedDict

from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers

from .models import Booking, Cleaning, CleaningStaff, Room, User


class TimeLine:
    def __init__(self, start: datetime.datetime = datetime.datetime.now() - datetime.timedelta(30),
                 end: datetime.datetime = datetime.datetime.now() + datetime.timedelta(30)):
        self.__inner_counter = OrderedDict()
        self.__inner_counter[(start, end)] = 1

    def get_timeline(self):
        return list(sorted(self.__inner_counter.keys()))

    def remove_slice(self, start: datetime.datetime, end: datetime.datetime):
        for key in self.__inner_counter.keys():
            if key[0].timestamp() <= start.timestamp() <= key[1].timestamp() and key[0].timestamp() \
                    <= end.timestamp() <= key[1].timestamp():
                del self.__inner_counter[key]
                self.__split_start(start, key)
                self.__split_end(start, key)
            elif key[0].timestamp() <= start.timestamp() <= key[1].timestamp():
                del self.__inner_counter[key]
                self.__split_start(start, key)
            elif key[0].timestamp() <= end.timestamp() <= key[1].timestamp():
                del self.__inner_counter[key]
                self.__split_end(start, key)
        return self

    def __split_start(self, start: datetime.datetime, key: tuple[datetime.datetime]):
        if start != key[0]:
            self.__inner_counter[(key[0], start)] = 1

    def __split_end(self, end: datetime.datetime, key: tuple[datetime.datetime]):
        if end != key[1]:
            self.__inner_counter[(end, key[1])] = 1


class CountObj:
    def __init__(self, count):
        self.count = count


class CountSerializer(serializers.Serializer):
    count = serializers.IntegerField()


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "middle_name", "last_name", "passport", "city", "is_admin")


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
    guest = GuestSerializer()

    class Meta:
        model = Booking
        fields = "__all__"


class BookingCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class GuestWithBookingSerializer(serializers.ModelSerializer):
    bookings_guest = BookingSerializer(many=True)
    curr_booking = serializers.SerializerMethodField()

    def get_curr_booking(self, obj: User):
        booking = None
        qs = obj.bookings_guest.filter(check_in__lte=datetime.datetime.now(),
                                       check_out__gte=datetime.datetime.now())
        if qs.count() > 0:
            booking = qs.get().id
        return booking

    class Meta:
        model = User
        fields = ("id", "first_name", "middle_name", "last_name", "passport", "city", "bookings_guest", "curr_booking",
                  "is_admin")


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class AllRoomSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True)
    is_free = serializers.SerializerMethodField()
    curr_booking = serializers.SerializerMethodField()

    def get_curr_booking(self, obj: Room):
        booking = None
        qs = obj.bookings.filter(check_in__lte=datetime.datetime.now(), check_out__gte=datetime.datetime.now())
        if qs.count() > 0:
            booking = qs.get().id
        return booking

    def get_is_free(self, obj: Room):
        return obj.bookings.filter(check_out__gte=datetime.datetime.now(),
                                   check_in__lte=datetime.datetime.now()).count() == 0

    class Meta:
        model = Room
        fields = "__all__"


class RoomWithFreeSerializer(serializers.ModelSerializer):
    free_time = serializers.SerializerMethodField()

    def get_free_time(self, obj: Room):
        timeline = TimeLine()
        map(lambda booking: timeline.remove_slice(datetime.datetime.fromtimestamp(booking.check_in.timestamp()),
                                                  datetime.datetime.fromtimestamp(booking.check_out.timestamp())),
            obj.bookings.filter(check_in__gte=datetime.datetime.now() - datetime.timedelta(days=30),
                                check_out__lte=datetime.datetime.now() + datetime.timedelta(days=30)))
        return timeline.get_timeline()

    class Meta:
        model = Room
        fields = "__all__"


class ReportObj:
    class RoomObj:
        def __init__(self, number: str, count: int, profit: float):
            self.number = number
            self.count = count
            self.profit = profit

    class FloorObj:
        def __init__(self, floor: str, count: int):
            self.floor = floor
            self.count = count

    def __init__(self, rooms: list[RoomObj], floors: list[FloorObj], profit: float):
        self.rooms = rooms
        self.floors = floors
        self.profit = profit


class ReportSerializer(serializers.Serializer):
    class RoomSerializer(serializers.Serializer):
        number = serializers.CharField()
        count = serializers.IntegerField()
        profit = serializers.FloatField()

    class FloorSerializer(serializers.Serializer):
        floor = serializers.CharField()
        count = serializers.IntegerField()

    rooms = RoomSerializer(many=True)
    floors = FloorSerializer(many=True)
    profit = serializers.FloatField()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = (
            "username", "password", "email", "first_name", "last_name", "middle_name", "passport", "city", "is_admin")
