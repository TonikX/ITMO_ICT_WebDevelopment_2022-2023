from rest_framework.generics import *
from .serializers import *


class ScenarioListAPIView(ListAPIView):
    serializer_class = ScenarioSerializer

    def get_queryset(self):
        game_systems = self.request.query_params.getlist('game_system')
        tags = self.request.query_params.getlist('tag')
        adult = self.request.query_params.get('adult')
        finished = self.request.query_params.get('finished')

        # Game Systems Filtering
        if len(game_systems) == 0:
            game_systems = GameSystem.objects.all()

        queryset = Scenario.objects.filter(game_system__id__in=game_systems)

        # Checkbox filtering
        if adult is None:
            queryset = queryset.filter(is_age_restricted=False)
        if finished is not None:
            queryset = queryset.filter(is_completed=True)

        # Tags filtering
        if len(tags) == 0:
            return queryset

        ids_to_exclude = []
        for el in queryset:
            object_tags = el.tags.values()
            count_tag = 0
            for tag in object_tags:
                if str(tag['id']) in tags:
                    count_tag += 1
            if count_tag < len(tags):
                ids_to_exclude.append(el.id)

        queryset = queryset.exclude(id__in=ids_to_exclude)

        return queryset


class ScenarioAPIView(RetrieveAPIView):
    serializer_class = ScenarioSerializer
    queryset = Scenario.objects.all()


class ScenarioCreateAPIView(CreateAPIView):
    serializer_class = ScenarioCreateUpdateSerializer


class ScenarioUpdateAPIView(UpdateAPIView):
    serializer_class = ScenarioCreateUpdateSerializer

    def get_object(self):
        scenario_id = self.kwargs['pk']
        return Scenario.objects.get(pk=scenario_id)


class ScenarioDestroyAPIView(DestroyAPIView):
    serializer_class = ScenarioCreateUpdateSerializer

    def get_object(self):
        scenario_id = self.kwargs['pk']
        return Scenario.objects.get(pk=scenario_id)


class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewCreateUpdateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['scenario_id'] = self.kwargs['scenario']
        return context


class ReviewUpdateAPIView(UpdateAPIView):
    serializer_class = ReviewCreateUpdateSerializer

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
