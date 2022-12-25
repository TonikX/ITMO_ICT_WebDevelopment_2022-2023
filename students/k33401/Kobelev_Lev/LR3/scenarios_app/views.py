from requests import Response
from rest_framework.generics import *
from rest_framework.views import APIView
from .serializers import *


class ScenarioListAPIView(ListAPIView):
    serializer_class = ScenarioSerializer
    queryset = Scenario.objects.all()


class ScenarioAPIView(RetrieveAPIView):
    serializer_class = ScenarioSerializer
    queryset = Scenario.objects.all()


class ScenarioCreateAPIView(CreateAPIView):
    serializer_class = ScenarioCreateSerializer


class ScenarioUpdateAPIView(UpdateAPIView):
    serializer_class = ScenarioUpdateSerializer

    def get_object(self):
        scenario_id = self.kwargs['pk']
        return Scenario.objects.get(pk=scenario_id)


class ScenarioDestroyAPIView(DestroyAPIView):
    serializer_class = ScenarioUpdateSerializer

    def get_object(self):
        scenario_id = self.kwargs['pk']
        return Scenario.objects.get(pk=scenario_id)


class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewCreateSerializer

    def get_serializer_context(self):
        return {'scenario_id': self.kwargs['scenario']}


class ReviewUpdateAPIView(UpdateAPIView):
    serializer_class = ReviewUpdateSerializer

    def get_object(self):
        scenario_id = self.kwargs['scenario']
        review_number = self.kwargs['review']
        return Review.objects.filter(scenario=scenario_id).order_by('-publish_date')[review_number]


class ScenarioLikesUpdateAPIView(UpdateAPIView):
    serializer_class = ScenarioLikeSerializer

    def get_object(self):
        scenario_id = self.kwargs['scenario']
        return Scenario.objects.get(pk=scenario_id)


class TagListAPIView(ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagCreateAPIView(CreateAPIView):
    serializer_class = TagSerializer


class GameSystemListAPIView(ListAPIView):
    serializer_class = GameSystemSerializer
    queryset = GameSystem.objects.all()


class GameSystemCreateAPIView(CreateAPIView):
    serializer_class = GameSystemSerializer
