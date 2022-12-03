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




class GuestListAPIView(ListAPIView):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()

class GuestCreateAPIView(CreateAPIView):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()

class GuestRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()

class GuestRetrieveAPIView(RetrieveAPIView):
    serializer_class = GuestRetrieveSerializer
    queryset = Guest.objects.all()




class CleanersListAPIView(ListAPIView):
    serializer_class = CleanersSerializer
    queryset = Cleaners.objects.all()

class CleanersCreateAPIView(CreateAPIView):
    serializer_class = CleanersSerializer
    queryset = Cleaners.objects.all()

class CleanersRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CleanersSerializer
    queryset = Cleaners.objects.all()

class CleanersRetrieveAPIView(RetrieveAPIView):
    serializer_class = CleanersSerializer
    queryset = Cleaners.objects.all()



class CleaningListAPIView(ListAPIView):
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()

class CleaningCreateAPIView(CreateAPIView):
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()




class BookingListAPIView(ListAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

class BookingCreateAPIView(CreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()



class AvailableRoomAPIView(ListAPIView):
    serializer_class = AvailableRoomSerializer

    def get_queryset(self):
        return Room.objects.all().filter(status="+")