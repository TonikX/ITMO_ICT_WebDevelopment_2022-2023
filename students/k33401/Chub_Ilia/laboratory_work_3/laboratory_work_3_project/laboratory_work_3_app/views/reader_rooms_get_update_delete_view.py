from rest_framework.generics import RetrieveUpdateDestroyAPIView
from ..serializers import ReaderRoomSerializer
from ..models import ReaderRoomModel


class ReaderRoomsGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderRoomSerializer
    queryset = ReaderRoomModel.objects.all()
