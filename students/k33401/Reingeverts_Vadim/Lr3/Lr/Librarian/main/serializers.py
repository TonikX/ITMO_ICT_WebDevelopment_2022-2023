from django.contrib.auth.hashers import make_password
from operator import itemgetter
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

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

    def validate(self, data):
        return data


class UserSerializer(ModelSerializer):
    model = models.User

    class Meta:
        model = models.User
        fields = "__all__"

        fields = [
            "username",
            "password",

            "last_name",
            "first_name",
            "middle_name",

            "serial_number",
            "passport",
            "address",
            "education_level",
            "phone_number",
        ]

    def create(self, validated_data):
        # Put list of keys to separate variables, aka destructuring assignment
        password = itemgetter(*['password'])(validated_data)
        # Get dict, excluding the keys that were 'taken out'
        rest = {key: validated_data[key]
                for key in validated_data if key not in ['password']}

        object = self.model.objects.create(
            password=make_password(password),
            serial_number=self.model.generate_random_serial(),
            **rest
        )

        return object

    def validate(self, data):

        reading_room = data.get("reading_room")
        if reading_room:
            if reading_room.get_empty_slots() - 1 < 0:
                raise ValidationError(
                    "There is not enough slots in this reading room")

        return data


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
