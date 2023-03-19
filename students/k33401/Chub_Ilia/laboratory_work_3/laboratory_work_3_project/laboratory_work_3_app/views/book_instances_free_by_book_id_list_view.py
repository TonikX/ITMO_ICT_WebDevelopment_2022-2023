from rest_framework.generics import ListAPIView
from ..serializers import BookInstanceSerializer
from ..models import BookInstanceModel, ReaderBookModel


class BookInstancesFreeByBookIdListView(ListAPIView):
    serializer_class = BookInstanceSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        book_instances = BookInstanceModel.objects\
            .filter(book_id=pk)\
            .exclude(id__in=ReaderBookModel.objects.values_list('book_instance_id', flat=True).all())

        return book_instances
