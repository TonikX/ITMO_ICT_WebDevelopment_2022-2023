# Serializers
## Tag
``` python
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
```
## Game System
``` python
class GameSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
```
## Review
- Получение:
``` python
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'author', 'publish_date', 'is_edited']
```
- Создание или обновление:
``` python
class ReviewCreateUpdateSerializer(serializers.Serializer):
    text = serializers.CharField()

    def create(self, validated_data):
        author = self.context['request'].user
        scenario_id = self.context['scenario_id']
        validated_data['scenario'] = Scenario.objects.get(pk=scenario_id)
        validated_data['author_id'] = User.objects.get(username=author).pk
        review = Review(**validated_data)
        review.save()
        return review

    def update(self, review, validated_data):
        review.text = validated_data['text']
        review.is_edited = True
        review.save()
        return review
```
## Scenario
- Получение:
``` python
class ScenarioSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    game_system = GameSystemSerializer()
    author = UserSerializer()
    likes = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField('get_reviews')

    def get_reviews(self, scenario):
        selected_reviews = Review.objects.filter(scenario=scenario.id)
        return ReviewSerializer(selected_reviews, many=True).data

    def get_likes(self, scenario):
        return scenario.likes.all().count()

    class Meta:
        model = Scenario
        fields = '__all__'
```
- Создание или обновление:
``` python
class ScenarioCreateUpdateSerializer(serializers.Serializer):
    tags = serializers.SlugRelatedField(queryset=Tag.objects.all(), slug_field='name', many=True)
    game_system = serializers.SlugRelatedField(queryset=GameSystem.objects.all(), slug_field='name')
    name = serializers.CharField(max_length=31)
    short_description = serializers.CharField(max_length=127)
    full_description = serializers.CharField()
    is_completed = serializers.BooleanField()
    is_age_restricted = serializers.BooleanField()

    def create(self, validated_data):
        author = self.context['request'].user
        validated_data['author_id'] = User.objects.get(username=author).pk
        tags = validated_data['tags']
        validated_data.pop('tags')
        scenario = Scenario(**validated_data)
        scenario.save()
        scenario.tags.set(tags)
        scenario.save()
        return scenario

    def update(self, scenario, validated_data):
        tags = scenario.tags.all()
        if 'tags' in validated_data:
            tags = validated_data['tags']
            validated_data.pop('tags')
        for attr, value in validated_data.items():
            setattr(scenario, attr, value)
        scenario.tags.set(tags)
        scenario.save()
        return scenario
```
- Обновление лайков:
``` python
class ScenarioLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = ['likes']

    def update(self, scenario, validated_data):
        user = self.context['request'].user

        if user in scenario.likes.all():
            scenario.likes.remove(User.objects.get(id=user.id))
        else:
            scenario.likes.add(User.objects.get(id=user.id))

        return scenario
```