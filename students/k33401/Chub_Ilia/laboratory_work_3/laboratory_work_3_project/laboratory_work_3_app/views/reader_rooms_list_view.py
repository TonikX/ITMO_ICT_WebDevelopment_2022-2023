from rest_framework.generics import ListAPIView
from ..serializers import ReaderRoomSerializer
from ..models import ReaderRoomModel


class ReaderRoomsListView(ListAPIView):
    serializer_class = ReaderRoomSerializer
    queryset = ReaderRoomModel.objects.all()
