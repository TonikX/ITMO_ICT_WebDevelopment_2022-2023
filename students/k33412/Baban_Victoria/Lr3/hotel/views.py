from django.db.models import Q, Count
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework import serializers, status
from rest_framework.response import Response
from .serializers import *
from datetime import datetime
from datetime import date
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import *


# просмотр всех гостей отеля
class AllGuests(ListAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


# просмотр всех бронирований
class AllBookings(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


# просмотр всех работников
class AllWorkers(ListAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer


# создание гостя
class CreateGuest(CreateAPIView, ListAPIView):
    queryset = Guest.objects.all()
    serializer_class = CreateGuestSerializer


# создание бронирования
class CreateBooking(CreateAPIView):
    serializer_class = CreateBookingSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = datetime.date(datetime.now())
        book = Room.objects.filter(Q(booking_room__date_end__lt=today) |
                                   Q(booking_room__date_start__gt=today) |
                                   Q(booking_room__isnull=True)).distinct()
        serializer = BookSerializerOnlyRoom(book, many=True)
        return Response({"Свободные номера на сегодня": serializer.data})

    def post(self, request, **kwargs):
        serializer = BookingSerializer(data=request.data)
        needed_books = Room.objects.exclude(
            Q(booking_room__date_end__gt=datetime.now(), booking_room__date_start__lt=datetime.now())).distinct()
        if len(needed_books) == 0:
            return Response("Нет свободных мест на текущую дату", status=status.HTTP_400_BAD_REQUEST)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Бронирование создано", status=status.HTTP_201_CREATED)


# создание работника
class CreateWorker(CreateAPIView, ListAPIView):
    queryset = Workers.objects.all()
    serializer_class = CreateWorkerSerializer


# количество гостей из заданного города
class GuestsByCity(RetrieveAPIView):
    lookup_field = "city"
    queryset = Guest.objects.all()
    serializer_class = CountSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            CountObj(self.queryset.filter(**{self.lookup_field: kwargs[self.lookup_field]}).count())
        )
        return Response(serializer.data)


# гости, проживающие в заданном номере в заданный период
class GuestsByPeriod(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = GuestsByPeriodSerializer

    def get_queryset(self):
        return self.queryset.filter(
            Q(date_start__gte=self.kwargs["period_date_start"], date_end__lte=self.kwargs["period_date_end"]) |
            Q(date_start__lte=self.kwargs["period_date_end"], date_end__gte=self.kwargs["period_date_start"]),
            room_number=self.kwargs["room_number"]
        )


# кто убирает в указанный день в номере указанного клиента
class GetWorkerByDayAndClient(APIView):
    def get(self, request, **kwargs):
        worker = Cleaning.objects.filter(day_of_week=kwargs["day_of_week"],
                                         floor__in=Room.objects.filter(
                                             booking_room__guest=kwargs["guest_passport"]).values(
                                             "floor"))
        serializer = CleaningSerializer(worker, many=True)
        return Response(serializer.data)


# количество свободных номеров на сегодня
class FreeRoomsCount(RetrieveAPIView):
    serializer_class = CountSerializer

    def filtered_queryset(self):
        return Room.objects.exclude(
            Q(booking_room__date_end__gt=datetime.now(), booking_room__date_start__lt=datetime.now())).distinct()

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            CountObj(self.filtered_queryset().count())
        )
        return Response(serializer.data)


# список клиентов с указанием места жительства, которые проживали в те же дни, что и заданный клиент, в определенный период времени.
class GuestsSamePeriods(APIView):
    def get(self, request, *args, **kwargs):
        result = []
        needed_guests_bookings = Guest.objects.get(passport=kwargs["passport"]).booking_guest.filter(
            Q(date_start__gte=self.kwargs["period_date_start"], date_end__lte=self.kwargs["period_date_end"]) |
            Q(date_start__lte=self.kwargs["period_date_end"], date_end__gte=self.kwargs["period_date_start"]))

        for booking in needed_guests_bookings:
            result += [booking.guest for booking in Booking.objects.filter(
                Q(date_start__gte=booking.date_start, date_end__lte=booking.date_end) |
                Q(date_start__lte=booking.date_end, date_end__gte=booking.date_start)
            ).exclude(guest__passport=kwargs["passport"])
                       ]

        serializer = GuestSerializer(result, many=True)
        return Response(serializer.data)


#квартальный отчет
class QReport(APIView):
    def get(self, *args, **kwargs):
        if kwargs["quarter"] == 1:
            filter = Q(date_start__gte=date(datetime.today().year, 1, 1),
                         date_start__lt=date(datetime.today().year, 3, 31))
        elif kwargs["quarter"] == 2:
            filter = Q(date_start__gte=date(datetime.today().year, 4, 1),
                         date_start__lt=date(datetime.today().year, 6, 30))
        elif kwargs["quarter"] == 3:
            filter = Q(date_start__gte=date(datetime.today().year, 7, 1),
                         date_start__lt=date(datetime.today().year, 9, 30))
        elif kwargs["quarter"] == 4:
            filter = Q(date_start__gte=date(datetime.today().year, 10, 1),
                         date_start__lt=date(datetime.today().year, 12, 31))

        floors = []
        for f in Room.objects.values("floor").annotate(Count("room_number")):
            floors.append({"floor": f["floor"], "count": f["room_number__count"]})

        rooms = []
        for room in Room.objects.all():
            counter = 0
            for booking in room.booking_room.filter(filter):
                counter += 1
            rooms.append(
                {
                    "name": room.room_number,
                    "count": counter,
                    "profit": booking.total_price
                }
            )

        total_profit = sum(r["profit"] for r in rooms)

        return render(
            self.request,
            "report.html",
            {"rooms": rooms, "floors": floors, "profit": total_profit}
        )