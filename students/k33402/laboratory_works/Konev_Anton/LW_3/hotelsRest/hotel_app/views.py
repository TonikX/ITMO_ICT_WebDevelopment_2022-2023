import datetime

from django.db.models import Q, Count
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from hotel_app.models import Booking, Cleaning, Room, Guest
from hotel_app.serializers import LivingClientsBookingSerializer, StaffByCleaningSerializer, \
    GuestWithBookingSerializer, CountSerializer, CountObj


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
    queryset = Guest.objects.all()


class GetCleaningStaffByClientAndDay(APIView):
    serializer_class = StaffByCleaningSerializer

    def get(self, *args, **kwargs):
        staff = Cleaning.objects.filter(week_day=kwargs["weekday"],
                                        floor__in=Room.objects.filter(bookings__guest=kwargs["guest_id"]).values(
                                            "floor"))

        return Response(self.serializer_class(staff, many=True).data)


class FreeRoomsCount(AbstractCountView):
    queryset = Room.objects.all()

    def filtered_queryset(self):
        return self.queryset.filter(Q(bookings__check_out__lt=datetime.datetime.now()) |
                                    Q(bookings__check_in__gt=datetime.datetime.now()) | Q(
            bookings__isnull=True)).distinct()


class GetClientsSamePeriods(APIView):
    serializer_class = GuestWithBookingSerializer

    def get(self, *args, **kwargs):
        result = []

        for booking in Guest.objects.get(id=kwargs["guest_id"]).bookings.all():
            result += [booking.guest for booking in
                       Booking.objects.filter(
                           Q(check_out__gte=booking.check_in, check_in__lte=booking.check_in) |
                           Q(check_in__gte=booking.check_in, check_in__lte=booking.check_out)
                       ).exclude(guest_id=kwargs["guest_id"])
                       ]

            return Response(self.serializer_class(result, many=True).data)


class QReport(APIView):
    def get(self, *args, **kwargs):
        if kwargs["q"] == 1:
            q_filter = Q(check_in__gte=datetime.date(datetime.date.today().year, 1, 1),
                         check_in__lt=datetime.date(datetime.date.today().year, 3, 31))
        elif kwargs["q"] == 2:
            q_filter = Q(check_in__gte=datetime.date(datetime.date.today().year, 4, 1),
                         check_in__lt=datetime.date(datetime.date.today().year, 6, 30))
        elif kwargs["q"] == 3:
            q_filter = Q(check_in__gte=datetime.date(datetime.date.today().year, 7, 1),
                         check_in__lt=datetime.date(datetime.date.today().year, 9, 30))
        elif kwargs["q"] == 4:
            q_filter = Q(check_in__gte=datetime.date(datetime.date.today().year, 10, 1),
                         check_in__lt=datetime.date(datetime.date.today().year, 12, 31))

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

        return render(
            self.request,
            "report.html",
            {"rooms": rooms, "floors": floors, "profit": sum(r["profit"] for r in rooms)}
        )
