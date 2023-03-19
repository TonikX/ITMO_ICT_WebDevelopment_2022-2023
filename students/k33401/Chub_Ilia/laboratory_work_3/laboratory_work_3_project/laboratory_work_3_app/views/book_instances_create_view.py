from rest_framework.generics import CreateAPIView
from ..serializers import BookInstanceSerializer
from ..models import BookInstanceModel


class BookInstancesCreateView(CreateAPIView):
    serializer_class = BookInstanceSerializer
    queryset = BookInstanceModel.objects.all()
