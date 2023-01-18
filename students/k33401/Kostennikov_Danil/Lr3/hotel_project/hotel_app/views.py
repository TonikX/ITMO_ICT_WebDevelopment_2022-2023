from django.shortcuts import render
# from rest_framework.generics import ListAPIView

from .models import *
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from datetime import datetime
from rest_framework.permissions import IsAdminUser
from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models import Q, Count


class CountObj:
    def __init__(self, count):
        self.count = count


class ClientsLivingPeriod(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingFieldRoomSerializer

    def get_queryset(self):
        return self.queryset.filter(
            Q(checkInDate__gte=self.kwargs["checkInDate"], checkOutDate__lte=self.kwargs["checkOutDate"]) |
            Q(checkInDate__lte=self.kwargs["checkInDate"], checkOutDate__gte=self.kwargs["checkOutDate"]),

            room=self.kwargs["room"]
        )


class ClientsCountByCity(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = CountSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            CountObj(self.queryset.filter(homeTown=self.kwargs["homeTown"]).count())
        )
        return Response(serializer.data)


class FreeRoomsCount(generics.RetrieveAPIView):
    serializer_class = CountSerializer
    queryset = Room.objects.all()

    def fitration(self, *args, **kwargs):
        return self.queryset.filter(Q(booking__checkInDate__lte=self.kwargs["date"]) &
                                    Q(booking__checkOutDate__gt=self.kwargs["date"])).distinct()

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            CountObj(self.queryset.count() - self.fitration().count())
        )
        return Response(serializer.data)


class ClientsSamePeriods(generics.RetrieveAPIView):
    serializer_class = CountSerializer

    def fitration(self, *args, **kwargs):
        result = []
        client = Client.objects.filter(passport=self.kwargs["client"]).first()
        for booking in Booking.objects.filter(client=client).all():
            result += Booking.objects.filter(Q(checkOutDate__gte=booking.checkOutDate) &
                                             Q(checkInDate__lte=booking.checkInDate) &
                                             Q(client__homeTown__isnull=False)).exclude(
                client__passport=self.kwargs["client"])
        return result

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            CountObj(len(self.fitration()))
        )
        return Response(serializer.data)


class EmployeesCleaning(APIView):
    # queryset = Room.objects.all()
    def get(self, *args, **kwargs):
        bookings = Booking.objects.filter(client__passport=kwargs["client"]).all()
        result = Employee.objects.none()
        for booking in bookings:
            result |= Cleening.objects.filter(Q(day__lte=booking.checkOutDate) &
                                              Q(day__gte=booking.checkInDate) &
                                              Q(day=kwargs["day"]) &
                                              Q(room=booking.room)).all()
        serializer = CleaningSerializer(result, many=True)
        return Response(serializer.data)


class Report(APIView):
    def get(self, *args, **kwargs):

        if kwargs["quarter"] == 1:
            quarterFilter = Q(checkInDate__gte=datetime(datetime.today().year, 1, 1),
                              checkInDate__lt=datetime(datetime.today().year, 3, 31))
        elif kwargs["quarter"] == 2:
            quarterFilter = Q(checkInDate__gte=datetime(datetime.today().year, 4, 1),
                              checkInDate__lt=datetime(datetime.today().year, 6, 30))
        elif kwargs["quarter"] == 3:
            quarterFilter = Q(checkInDate__gte=datetime(datetime.today().year, 7, 1),
                              checkInDate__lt=datetime(datetime.today().year, 9, 30))
        elif kwargs["quarter"] == 4:
            quarterFilter = Q(ccheckInDate__gte=datetime(datetime.today().year, 10, 1),
                              checkInDate__lt=datetime(datetime.today().year, 12, 31))

        floors = []
        for f in Room.objects.values("number").annotate(Count("id")):
            floors.append({"floor": int(f["number"] / 10), "count": f["id__count"]})

        rooms = []
        for room in Room.objects.all():
            days = 0
            counter = 0
            for booking in room.booking_set.filter(quarterFilter):
                days += (booking.checkOutDate - booking.checkInDate).days
                counter += 1
            rooms.append(
                {
                    "name": room.number,
                    "count": counter,
                    "profit": room.roomType.pricePerNight * days
                }
            )

        return render(
            self.request,
            "report.html",
            {"floors": floors, "rooms": rooms, "profit": sum(r["profit"] for r in rooms)}
        )


# admin views
class CreateEmployee(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]
    queryset = Employee.objects.all()


class DeleteEmployee(generics.DestroyAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]
    queryset = Employee.objects.all()


class UpdateEmployee(generics.UpdateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]
    queryset = Employee.objects.all()


class CreateBooking(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAdminUser]
    queryset = Booking.objects.all()


class DeleteBooking(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class UpdateBooking(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
