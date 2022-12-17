import datetime
import os
from typing import Optional

from django.core.exceptions import ValidationError
from django.db.models import Q, Count
from django.http import HttpResponse
from docxtpl import DocxTemplate
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from hotel_app.models import Booking, Cleaning, Room
from hotel_app.serializers import LivingClientsBookingSerializer, StaffByCleaningSerializer, \
    GuestWithBookingSerializer
from hotelsRest.settings import BASE_DIR
from users_app.models import User


class LivingClientsListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = LivingClientsBookingSerializer

    def get_queryset(self):
        from_date_str: Optional[str] = self.kwargs.get("fromDate", None)
        to_date_str: Optional[str] = self.kwargs.get("toDate", None)

        if not (from_date_str and to_date_str):
            raise ValidationError("fromDate and toDate must be set")

        try:
            from_date = datetime.datetime.strptime(from_date_str, "%Y-%m-%d %H:%M:%S")
            to_date = datetime.datetime.strptime(to_date_str, "%Y-%m-%d %H:%M:%S")
        except:
            raise ValidationError("fromDate or toDate is invalid format use Y-%m-%d %H:%M:%S")

        queryset = super(LivingClientsListView, self).get_queryset().filter(
            Q(check_in__gte=from_date, check_in__lte=to_date) | Q(check_out__gte=to_date, check_out__lte=from_date))
        return queryset


class LivingClientsByRoomListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = LivingClientsBookingSerializer

    def get_queryset(self):
        from_date_str: Optional[str] = self.kwargs.get("fromDate", None)
        to_date_str: Optional[str] = self.kwargs.get("toDate", None)

        if not (from_date_str and to_date_str):
            raise ValidationError("fromDate and toDate must be set")

        try:
            from_date = datetime.datetime.strptime(from_date_str, "%Y-%m-%d %H:%M:%S")
            to_date = datetime.datetime.strptime(to_date_str, "%Y-%m-%d %H:%M:%S")
        except:
            raise ValidationError("fromDate or toDate is invalid format use Y-%m-%d %H:%M:%S")

        queryset = super(LivingClientsByRoomListView, self).get_queryset().filter(
            Q(check_in__gte=from_date, check_in__lte=to_date) | Q(check_out__gte=to_date, check_out__lte=from_date),
            room__id=self.kwargs["roomId"])
        return queryset


class ClientsFromCityView(APIView):
    def get(self, *a, **kw):
        return Response("{\"count\": " + str(User.objects.filter(is_cleaning_staff=False, is_superuser=False,
                                                                 city=kw["city"]).count()) + "}")


class GetCleaningStaffByClientAndWeekDay(APIView):
    serializer_class = StaffByCleaningSerializer

    def get(self, *a, **kw):
        staff = Cleaning.objects.filter(week_day=kw["weekday"],
                                        floor__in=Room.objects.filter(bookings__guest=kw["guestId"]).values("floor"))

        return Response(self.serializer_class(staff, many=True).data)


class FreeRoomsCountView(APIView):
    def get(self, *a, **kw):
        return Response("{\"count\": " + str(Room.objects.filter(Q(bookings__check_in__gt=datetime.datetime.now()) |
                                                                 Q(bookings__check_out__lt=datetime.datetime.now()) | Q(
            bookings__isnull=True)).count()) + "}")


class GetClientsWithSamePeriod(APIView):
    serializer_class = GuestWithBookingSerializer

    def get(self, *a, **kw):
        guests = User.objects.filter(is_cleaning_staff=False, is_superuser=False, bookings__check_in__lte=kw["toDate"],
                                     bookings__check_out__gte=kw["fromDate"]).exclude(id=kw["guestId"])

        return Response(self.serializer_class(guests, many=True).data)


class QuartalReport(APIView):
    def get(self, *a, **kw):
        if kw["q"] == 1:
            q_filter = Q(check_in__gte=datetime.date(datetime.date.today().year, 1, 1),
                         check_in__lt=datetime.date(datetime.date.today().year, 3, 31))
        elif kw["q"] == 2:
            q_filter = Q(check_in__gte=datetime.date(datetime.date.today().year, 4, 1),
                         check_in__lt=datetime.date(datetime.date.today().year, 6, 31))
        elif kw["q"] == 3:
            q_filter = Q(check_in__gte=datetime.date(datetime.date.today().year, 7, 1),
                         check_in__lt=datetime.date(datetime.date.today().year, 9, 31))
        else:
            q_filter = Q(check_in__gte=datetime.date(datetime.date.today().year, 10, 1),
                         check_in__lt=datetime.date(datetime.date.today().year, 12, 31))

        floors = []
        for f in Room.objects.values("floor").annotate(Count("id")):
            floors.append({"floor": f["floor"], "count": f["id__count"]})

        rooms = []
        for r in Room.objects.all():
            days = 0
            c = 0
            for b in r.bookings.filter(q_filter):
                days += (b.check_out - b.check_in).days
                c += 1
            rooms.append(
                {
                    "name": r.number,
                    "count": c,
                    "profit": r.price * days
                }
            )
        doc = DocxTemplate(os.path.join(BASE_DIR, 'templates/report.docx'))
        doc.render({"rooms": rooms, "floors": floors, "profit": sum(r["profit"] for r in rooms)})
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename = "report' + '.docx"'
        doc.save(response)

        return response
