# Views
## Scenario (сценарии)
- Все списком:
``` python
class ScenarioListAPIView(ListAPIView):
    serializer_class = ScenarioSerializer
    queryset = Scenario.objects.all()
```
- Конкретный:
``` python
class ScenarioAPIView(RetrieveAPIView):
    serializer_class = ScenarioSerializer
    queryset = Scenario.objects.all()
```
- Создать:
``` python
class ScenarioCreateAPIView(CreateAPIView):
    serializer_class = ScenarioCreateUpdateSerializer
```
- Обновить:
``` python
class ScenarioUpdateAPIView(UpdateAPIView):
    serializer_class = ScenarioCreateUpdateSerializer

    def get_object(self):
        scenario_id = self.kwargs['pk']
        return Scenario.objects.get(pk=scenario_id)
```
- Удалить:
``` python
class ScenarioDestroyAPIView(DestroyAPIView):
    serializer_class = ScenarioCreateUpdateSerializer

    def get_object(self):
        scenario_id = self.kwargs['pk']
        return Scenario.objects.get(pk=scenario_id)
```
- Обновить лайки:
``` python
class ScenarioLikesUpdateAPIView(UpdateAPIView):
    serializer_class = ScenarioLikeSerializer

    def get_object(self):
        scenario_id = self.kwargs['scenario']
        return Scenario.objects.get(pk=scenario_id)
```
## Tags (тэги)
- Все списком:
``` python
class TagListAPIView(ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
```
- Создать:
``` python
class TagCreateAPIView(CreateAPIView):
    serializer_class = TagSerializer
```
## Game Systems (системы):
- Все списком:
``` python
class GameSystemListAPIView(ListAPIView):
    serializer_class = GameSystemSerializer
    queryset = GameSystem.objects.all()
```
- Создать:
``` python
class GameSystemCreateAPIView(CreateAPIView):
    serializer_class = GameSystemSerializer
```
## Reviews (обзоры):
- Создать:
``` python
class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewCreateUpdateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['scenario_id'] = self.kwargs['scenario']
        return context
```
- Обновить:
``` python
class ReviewUpdateAPIView(UpdateAPIView):
    serializer_class = ReviewCreateUpdateSerializer

    def get_object(self):
        scenario_id = self.kwargs['scenario']
        review_number = self.kwargs['review']
        return Review.objects.filter(scenario=scenario_id).order_by('-publish_date')[review_number]
```