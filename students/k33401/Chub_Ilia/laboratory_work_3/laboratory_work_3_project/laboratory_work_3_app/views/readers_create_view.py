from rest_framework.generics import CreateAPIView
from ..serializers import ReaderSerializer
from ..models import ReaderModel


class ReadersCreateView(CreateAPIView):
    serializer_class = ReaderSerializer
    queryset = ReaderModel.objects.all()
