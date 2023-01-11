from .serializers import *
from rest_framework.generics import *


class RoomListAPIView(ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomCreateAPIView(CreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomRetrieveAPIView(RetrieveAPIView):
    serializer_class = RoomRetrieveSerializer
    queryset = Room.objects.all()


class ClientListAPIView(ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientCreateAPIView(CreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientRetrieveAPIView(RetrieveAPIView):
    serializer_class = ClientRetrieveSerializer
    queryset = Client.objects.all()


class EmployeeListAPIView(ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeCreateAPIView(CreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeRetrieveAPIView(RetrieveAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class BookingListAPIView(ListAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class BookingCreateAPIView(CreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()