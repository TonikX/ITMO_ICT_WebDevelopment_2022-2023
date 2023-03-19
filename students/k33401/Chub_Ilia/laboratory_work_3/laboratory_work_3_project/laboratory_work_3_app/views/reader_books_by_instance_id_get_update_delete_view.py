from rest_framework.generics import RetrieveUpdateDestroyAPIView
from ..serializers import ReaderBookSerializer
from ..models import ReaderBookModel


class ReaderBooksByInstanceIdGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderBookSerializer

    def get_object(self):
        pk = self.kwargs['pk']
        queryset = ReaderBookModel.objects.get(book_instance_id=pk)

        return queryset
