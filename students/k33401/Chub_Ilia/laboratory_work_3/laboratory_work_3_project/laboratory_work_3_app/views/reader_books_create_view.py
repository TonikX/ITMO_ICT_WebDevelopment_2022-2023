from rest_framework.generics import CreateAPIView
from ..serializers import ReaderBookCreateSerializer
from ..models import ReaderBookModel


class ReaderBooksCreateView(CreateAPIView):
    serializer_class = ReaderBookCreateSerializer
    queryset = ReaderBookModel.objects.all()
