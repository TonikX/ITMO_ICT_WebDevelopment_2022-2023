from rest_framework.generics import RetrieveUpdateDestroyAPIView
from ..serializers import BookInstanceSerializer
from ..models import BookInstanceModel


class BookInstancesGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookInstanceSerializer
    queryset = BookInstanceModel.objects.all()
