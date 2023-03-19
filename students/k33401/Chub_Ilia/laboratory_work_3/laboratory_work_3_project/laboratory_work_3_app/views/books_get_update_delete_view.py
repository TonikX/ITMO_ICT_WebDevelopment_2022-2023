from rest_framework.generics import RetrieveUpdateDestroyAPIView
from ..serializers import BookSerializer
from ..models import BookModel


class BooksGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = BookModel.objects.all()
