from rest_framework.generics import ListAPIView
from ..serializers import BookInstanceSerializer
from ..models import BookInstanceModel


class BookInstancesListView(ListAPIView):
    serializer_class = BookInstanceSerializer
    queryset = BookInstanceModel.objects.all()
