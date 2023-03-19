from rest_framework.generics import ListAPIView
from ..serializers import ReaderBookSerializer
from ..models import ReaderBookModel


class ReaderBooksByReaderListView(ListAPIView):
    serializer_class = ReaderBookSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = ReaderBookModel.objects.filter(reader=pk)

        return queryset
