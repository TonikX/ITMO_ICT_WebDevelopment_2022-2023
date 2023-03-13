from rest_framework.generics import RetrieveUpdateDestroyAPIView
from ..serializers import ReaderSerializer
from ..models import ReaderModel


class ReadersGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderSerializer
    queryset = ReaderModel.objects.all()
