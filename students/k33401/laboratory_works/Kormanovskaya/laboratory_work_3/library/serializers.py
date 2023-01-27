from django.db.models import Avg
from rest_framework import serializers
from .models import Book, Author, Genre, Reading, User, Achievement, UserAchievement


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = "__all__"


class AchievementUserSerializer(serializers.ModelSerializer):
    achievement = AchievementSerializer()

    class Meta:
        model = UserAchievement
        fields = "__all__"


class BookFullSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer(many=True)

    avg_rating = serializers.SerializerMethodField()

    def get_avg_rating(self, ob):
        return ob.reading.all().aggregate(Avg('rate'))['rate__avg']

    class Meta:
        model = Book
        fields = "__all__"


class GenreBookSerializer(serializers.ModelSerializer):
    book_set = BookSerializer(many=True)

    class Meta:
        model = Genre
        fields = ['name', 'book_set']


class AuthorBookSerializer(serializers.ModelSerializer):
    book_set = BookFullSerializer(many=True)

    class Meta:
        model = Author
        fields = ['name', 'book_set']


class ReadingSerializer(serializers.ModelSerializer):
    book = BookFullSerializer()

    class Meta:
        model = Reading
        fields = '__all__'


class ReadingCreateUpdateSerializer(serializers.Serializer):
    review_text = serializers.CharField(required=False, allow_null=True, default=None)
    rate = serializers.IntegerField(required=False, allow_null=True, default=None)
    is_read = serializers.BooleanField(required=False)

    def create(self, validated_data):
        user = self.context['request'].user
        book = self.context['book']
        validated_data['book_id'] = Book.objects.get(pk=book).pk
        validated_data['user_id'] = User.objects.get(username=user).pk
        reading = Reading(**validated_data)
        reading.save()
        return reading

    def update(self, reading, validated_data):
        reading.review_text = validated_data['review_text']
        reading.rate = validated_data['rate']
        reading.is_read = validated_data['is_read']
        reading.save()
        return reading


class UserSerializer(serializers.ModelSerializer):
    reading_set = ReadingSerializer(many=True)
    userachievement_set = AchievementUserSerializer(many=True)

    class Meta:
        model = User
        fields = ['username', 'reading_set', 'userachievement_set']


class UserInfoSerializer(serializers.ModelSerializer):
    reading_set = BookFullSerializer(many=True)
