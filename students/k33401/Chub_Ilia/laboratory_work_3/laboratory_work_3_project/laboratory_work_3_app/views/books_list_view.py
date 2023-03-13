from rest_framework.generics import ListAPIView
from ..serializers import BookSerializer
from ..models import BookModel


class BookListView(ListAPIView):
    serializer_class = BookSerializer
    queryset = BookModel.objects.all()
