from rest_framework.generics import RetrieveUpdateDestroyAPIView
from ..serializers import UserReaderSerializer
from ..models import UserReaderModel


class UserReaderGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserReaderSerializer
    queryset = UserReaderModel.objects.all()
