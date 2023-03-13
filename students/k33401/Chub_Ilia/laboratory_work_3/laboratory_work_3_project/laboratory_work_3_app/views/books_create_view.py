from rest_framework.generics import CreateAPIView
from ..serializers import BookSerializer
from ..models import BookModel


class BookCreateView(CreateAPIView):
    serializer_class = BookSerializer
    queryset = BookModel.objects.all()
