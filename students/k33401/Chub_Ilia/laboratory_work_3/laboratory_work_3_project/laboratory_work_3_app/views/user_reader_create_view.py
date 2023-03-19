from rest_framework.generics import CreateAPIView
from ..serializers import UserReaderSerializer
from ..models import UserReaderModel


class UserReaderCreateView(CreateAPIView):
    serializer_class = UserReaderSerializer
    queryset = UserReaderModel.objects.all()
