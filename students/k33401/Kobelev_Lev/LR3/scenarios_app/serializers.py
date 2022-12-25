from rest_framework import serializers
from .models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class GameSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        ref_name = 'User 1'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'author', 'publish_date', 'is_edited']


class ScenarioSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    game_system = GameSystemSerializer()
    author = UserSerializer()
    likes = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField('get_reviews')

    def get_reviews(self, obj):
        selected_reviews = Review.objects.filter(scenario=obj.id)
        return ReviewSerializer(selected_reviews, many=True).data

    def get_likes(self, obj):
        return obj.likes.all().count()

    class Meta:
        model = Scenario
        fields = '__all__'


class ScenarioCreateSerializer(serializers.Serializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
    game_system = serializers.SlugRelatedField(queryset=GameSystem.objects.all(), slug_field='name')
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    name = serializers.CharField(max_length=31)
    short_description = serializers.CharField(max_length=127)
    full_description = serializers.CharField()
    is_completed = serializers.BooleanField()
    is_age_restricted = serializers.BooleanField()

    def create(self, validated_data):
        tags = validated_data['tags']
        validated_data.pop('tags')
        scenario = Scenario(**validated_data)
        scenario.tags.set(tags)
        scenario.save()
        return scenario


class ScenarioUpdateSerializer(serializers.Serializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
    game_system = serializers.SlugRelatedField(queryset=GameSystem.objects.all(), slug_field='name')
    name = serializers.CharField(max_length=31)
    short_description = serializers.CharField(max_length=127)
    full_description = serializers.CharField()
    is_completed = serializers.BooleanField()
    is_age_restricted = serializers.BooleanField()

    def update(self, obj, validated_data):
        tags = validated_data['tags']
        validated_data.pop('tags')
        for attr, value in validated_data.items():
            setattr(obj, attr, value)
        obj.tags.set(tags)
        obj.save()
        return obj


class ReviewCreateSerializer(serializers.Serializer):
    scenario = serializers.SlugRelatedField(queryset=Scenario.objects.all(), slug_field='name')
    text = serializers.CharField()
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    def create(self, validated_data):
        scenario_id = self.context['scenario_id']
        validated_data['scenario'] = Scenario.objects.get(pk=scenario_id)
        review = Review(**validated_data)
        review.save()
        return Review(**validated_data)


class ReviewUpdateSerializer(serializers.Serializer):
    text = serializers.CharField()

    def update(self, obj, validated_data):
        obj.text = validated_data['text']
        obj.is_edited = True
        obj.save()
        return obj


class ScenarioLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = ['likes']

    def update(self, obj, validated_data):
        user = self.context['request'].user

        if user in obj.likes.all():
            obj.likes.remove(User.objects.get(id=user.id))
        else:
            obj.likes.add(User.objects.get(id=user.id))

        return obj
