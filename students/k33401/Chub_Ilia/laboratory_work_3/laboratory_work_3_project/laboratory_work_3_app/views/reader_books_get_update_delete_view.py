from rest_framework.generics import RetrieveUpdateDestroyAPIView
from ..serializers import ReaderBookSerializer
from ..models import ReaderBookModel


class ReaderBooksGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderBookSerializer
    queryset = ReaderBookModel.objects.all()
