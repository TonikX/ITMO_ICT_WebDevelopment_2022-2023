from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Country, City, UserChoice
from .serializers import CountrySerializer, CitySerializer, UserChoiceWriteSerializer, UserChoiceReadSerializer


class CountryViewSet(ReadOnlyModelViewSet):
    """Предаставление для стран (только чтение)"""
    queryset = Country.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CountrySerializer


class CityViewSet(ReadOnlyModelViewSet):
    """Предаставление для городов (только чтение)"""
    queryset = City.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CitySerializer


class UserChoiceViewSet(ModelViewSet):
    """Предаставление для выбранных городов"""
    queryset = UserChoice.objects.none()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        # При записи сериалайзер с id города, при чтении с подробной информацией о городе
        if self.action in ['retrieve', 'list']:
            return UserChoiceReadSerializer
        else:
            return UserChoiceWriteSerializer

    def get_queryset(self):
        # Фильтрует только выбор текущего пользователя
        print(self.request.user.pk)
        return UserChoice.objects.filter(user=self.request.user)
