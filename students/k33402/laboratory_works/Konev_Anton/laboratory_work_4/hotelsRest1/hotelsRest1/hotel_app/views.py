import datetime

from django.db.models import Q, Count
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Booking, Cleaning, Room, User
from .serializers import LivingClientsBookingSerializer, StaffByCleaningSerializer, \
    GuestWithBookingSerializer, CountSerializer, CountObj, RoomSerializer, BookingSerializer, RoomWithFreeSerializer, \
    AllRoomSerializer, ReportObj, ReportSerializer, BookingCreateUpdateSerializer


class AbstractCountView(RetrieveAPIView):
    serializer_class = CountSerializer

    def filtered_queryset(self, *args, **kwargs):
        return self.queryset.filter(**{self.lookup_field: kwargs[self.lookup_field]})

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            CountObj(self.filtered_queryset(*args, **kwargs).count())
        )
        return Response(serializer.data)


class LivingClients(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = LivingClientsBookingSerializer

    def get_queryset(self):
        return self.queryset.filter(
            Q(check_out__gte=self.kwargs["from_date"], check_in__lte=self.kwargs["from_date"]) |
            Q(check_in__gte=self.kwargs["from_date"], check_in__lte=self.kwargs["to_date"]),
            room_id=self.kwargs["room_id"]
        )


class ClientsByCity(AbstractCountView):
    lookup_field = "city"
    queryset = User.objects.all()


class GetCleaningStaffByClientAndDay(APIView):
    serializer_class = StaffByCleaningSerializer

    def get(self, *args, **kwargs):
        staff = Cleaning.objects.filter(week_day=kwargs["weekday"],
                                        floor__in=Room.objects.filter(bookings__guest=kwargs["guest_id"]).values(
                                            "floor"))

        return Response(self.serializer_class(staff, many=True).data)


class FreeRoomsList(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def filtered_queryset(self):
        return self.queryset.filter(Q(bookings__check_out__lt=datetime.datetime.now()) |
                                    Q(bookings__check_in__gt=datetime.datetime.now()) | Q(
            bookings__isnull=True))


class GetClientsSamePeriods(APIView):
    serializer_class = GuestWithBookingSerializer

    def get(self, *args, **kwargs):
        result = []

        for booking in User.objects.get(id=kwargs["guest_id"]).bookings_guest.all():
            result += [b.guest for b in
                       Booking.objects.filter(
                           Q(check_out__gte=booking.check_in, check_in__lte=booking.check_in) |
                           Q(check_in__gte=booking.check_in, check_in__lte=booking.check_out)
                       ).exclude(guest_id=kwargs["guest_id"])
                       ]

        return Response(self.serializer_class(result, many=True).data)


class QReport(APIView):
    def get(self, *args, **kwargs):
        match kwargs["q"]:
            case 1:
                q_filter = Q(check_in__gte=datetime.date(datetime.date.today().year, 1, 1),
                             check_in__lt=datetime.date(datetime.date.today().year, 3, 31))
            case 2:
                q_filter = Q(check_in__gte=datetime.date(datetime.date.today().year, 4, 1),
                             check_in__lt=datetime.date(datetime.date.today().year, 6, 31))
            case 3:
                q_filter = Q(check_in__gte=datetime.date(datetime.date.today().year, 7, 1),
                             check_in__lt=datetime.date(datetime.date.today().year, 9, 31))
            case 4:
                q_filter = Q(check_in__gte=datetime.date(datetime.date.today().year, 10, 1),
                             check_in__lt=datetime.date(datetime.date.today().year, 12, 31))
            case _:
                pass

        floors = []
        for f in Room.objects.values("floor").annotate(Count("id")):
            floors.append({"floor": f["floor"], "count": f["id__count"]})

        rooms = []
        for room in Room.objects.all():
            days = 0
            counter = 0
            for booking in room.bookings.filter(q_filter):
                days += (booking.check_out - booking.check_in).days
                counter += 1
            rooms.append(
                {
                    "name": room.number,
                    "count": counter,
                    "profit": room.price * days
                }
            )

        return Response(
            ReportSerializer(
                ReportObj(
                    [ReportObj.RoomObj(i["name"], i["count"], i["profit"]) for i in rooms],
                    [ReportObj.FloorObj(i["floor"], i["count"]) for i in floors],
                    sum(r["profit"] for r in rooms)
                )
            ).data
        )


class RoomsAvailable(ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    def get(self, *args, **kwargs):
        result = []
        queryset = self.get_queryset()
        if "room_type" in kwargs:
            queryset = queryset.filter(room_type=Room.ROOM_TYPES(kwargs["room_type"]))

        for room in queryset:
            is_ok = True
            for booking in room.bookings.all():
                if datetime.datetime.fromisoformat(
                        kwargs[
                            "start_ts"]).timestamp() < booking.check_in.timestamp() < datetime.datetime.fromisoformat(
                    kwargs["end_ts"]).timestamp() or datetime.datetime.fromisoformat(
                    kwargs["start_ts"]).timestamp() < booking.check_out.timestamp() < datetime.datetime.fromisoformat(
                    kwargs["end_ts"]).timestamp():
                    is_ok = False
                    break
            if is_ok:
                result.append(room)

        return Response(self.serializer_class(result, many=True).data)


class GuestBookingListCreate(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_serializer_class(self):
        if self.request.method != "POST":
            return self.serializer_class
        else:
            return BookingCreateUpdateSerializer


class GuestBookingUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_serializer_class(self):
        if self.request.method != "PUT":
            return self.serializer_class
        else:
            return BookingCreateUpdateSerializer


class ApproveBookingView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        booking = Booking.objects.get(id=kwargs["pk"])
        booking.approved = True
        booking.save()
        return Response("ok")


class CheckOutBookingNowView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        booking = Booking.objects.get(id=kwargs["pk"])
        booking.check_out = datetime.datetime.now()
        booking.save()
        return Response("ok")


class RoomsAllView(ListAPIView):
    serializer_class = AllRoomSerializer
    queryset = Room.objects.all()


class RoomWithFreeTimeView(ListAPIView):
    serializer_class = RoomWithFreeSerializer
    queryset = Room.objects.all()


class GuestsListView(ListAPIView):
    queryset = User.objects.filter(is_admin=False)
    serializer_class = GuestWithBookingSerializer


class GuestsGetView(RetrieveAPIView):
    queryset = User.objects.filter(is_admin=False)
    serializer_class = GuestWithBookingSerializer
