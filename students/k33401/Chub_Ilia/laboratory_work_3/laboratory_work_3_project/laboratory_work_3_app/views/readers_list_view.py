from rest_framework.generics import ListAPIView
from ..serializers import ReaderSerializer
from ..models import ReaderModel


class ReadersListView(ListAPIView):
    serializer_class = ReaderSerializer
    queryset = ReaderModel.objects.all()
