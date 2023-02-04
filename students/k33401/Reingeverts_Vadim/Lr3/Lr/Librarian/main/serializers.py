from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = "__all__"
        depth = 1


class LibrarySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Library
        fields = "__all__"
        depth = 1


class ReadingRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ReadingRoom
        fields = "__all__"
        depth = 1


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Book
        fields = "__all__"
        depth = 1


class ReadingRoomBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ReadingRoomBook
        fields = "__all__"
        depth = 1


class ReadingRoomBookUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ReadingRoomBookUser
        fields = "__all__"
        depth = 1


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
