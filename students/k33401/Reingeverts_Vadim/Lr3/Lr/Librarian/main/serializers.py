from rest_framework import serializers
from . import models


class ModelSerializer(serializers.ModelSerializer):
    model = None

    class Meta:
        model = None
        depth = 1

    def create(self, validated_data):
        object = self.model(**validated_data)
        object.save()
        return object


class UserSerializer(ModelSerializer):
    model = models.User

    class Meta:
        model = models.User
        fields = "__all__"


class LibrarySerializer(ModelSerializer):
    model = models.Library

    class Meta:
        model = models.Library
        fields = "__all__"


class ReadingRoomSerializer(ModelSerializer):
    model = models.ReadingRoom

    class Meta:
        model = models.ReadingRoom
        fields = "__all__"


class BookSerializer(ModelSerializer):
    model = models.Book

    class Meta:
        model = models.Book
        fields = "__all__"


class ReadingRoomBookSerializer(ModelSerializer):
    model = models.ReadingRoomBook

    class Meta:
        model = models.ReadingRoomBook
        fields = "__all__"


class ReadingRoomBookUserSerializer(ModelSerializer):
    model = models.ReadingRoomBookUser

    class Meta:
        model = models.ReadingRoomBookUser
        fields = "__all__"


# class ProfessionSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Profession
#         fields = "__all__"


# class ProfessionCreateSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=120)
#     description = serializers.CharField()

#     def create(self, validated_data):
#         profession = Profession(**validated_data)
#         profession.save()
#         return Profession(**validated_data)


# class SkillSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Skill
#         fields = "__all__"


# class SkillCreateSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=120)

#     def create(self, validated_data):
#         skill = Skill(**validated_data)
#         skill.save()
#         return Skill(**validated_data)


# class WarriorAndProfessionSerializer(serializers.ModelSerializer):

#     profession = ProfessionSerializer()

#     class Meta:
#         model = Warrior
#         fields = "__all__"


# class WarriorAndSkillSerializer(serializers.ModelSerializer):

#     # skill = SkillSerializer(many=True)
#     skill = serializers.StringRelatedField(read_only=True, many=True)

#     class Meta:
#         model = Warrior
#         fields = "__all__"


# class WarriorDetailsSerializer(serializers.ModelSerializer):

#     race = serializers.CharField(source="get_race_display", read_only=True)

#     class Meta:
#         model = Warrior
#         fields = "__all__"
#         depth = 1
