from rest_framework.generics import ListAPIView
from ..serializers import ReaderWithBookSerializer
from ..models import ReaderModel


class ReadersWithBooksListView(ListAPIView):
    serializer_class = ReaderWithBookSerializer
    queryset = ReaderModel.objects.all()
