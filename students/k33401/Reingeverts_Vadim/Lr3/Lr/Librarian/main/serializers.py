from django.contrib.auth.hashers import make_password
from operator import itemgetter
from rest_framework import serializers
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

        fields = [
            "id",
            "username",
            "password",
            "email",

            "last_name",
            "first_name",
            "middle_name",

            "serial_number",
            "passport",
            "address",
            "education_level",
            "phone_number",
            "academic_degree",
            "library",
            "reading_room",
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
                raise serializers.ValidationError(
                    {"error": "There is not enough slots in this reading room"})

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

    def validate(self, data):
        reading_room = self.instance
        capacity = data.get("capacity")
        if capacity is not None:
            users = reading_room.user_set

            if users.count() > capacity:
                raise serializers.ValidationError({"error":
                                                   "The amount of readers cannot exceed the capacity of the room"})
        return data


class BookSerializer(ModelSerializer):
    model = models.Book

    class Meta:
        model = models.Book
        fields = "__all__"

    def validate(self, data):
        book = self.instance

        prev_total_stock = book.total_stock
        new_total_stock = data.get("total_stock")
        if new_total_stock is not None:

            stock_diff = new_total_stock - prev_total_stock

            prev_undesignated_stock = book.get_undesignated_stock()
            new_undesignated_stock = prev_undesignated_stock + stock_diff

            if new_undesignated_stock < 0:
                raise serializers.ValidationError({"error":
                                                   "The amount of books designated to reading rooms cannot exceed the total stock"})

        return data


class ReadingRoomBookSerializer(ModelSerializer):
    model = models.ReadingRoomBook

    class Meta:
        model = models.ReadingRoomBook
        fields = "__all__"

    def validate(self, data):
        reading_room_book = self.instance
        book = reading_room_book.book

        prev_stock = reading_room_book.stock
        new_stock = data.get("stock")
        if new_stock is not None:
            stock_diff = new_stock - prev_stock

            prev_undesignated_stock = book.get_undesignated_stock()
            new_undesignated_stock = prev_undesignated_stock - stock_diff

            if stock_diff > 0 and new_undesignated_stock < 0:
                raise serializers.ValidationError({"error":
                                                   "Not enough undesignated books to restock this reading room"})

            prev_avaliable_stock = reading_room_book.get_avaliable_stock()
            new_avaliable_stock = prev_avaliable_stock + stock_diff

            if stock_diff < 0 and new_avaliable_stock < 0:
                raise serializers.ValidationError({"error":
                                                   "The reduction in stock exceeds the avaliable stock"})
        return data


class ReadingRoomBookUserSerializer(ModelSerializer):
    model = models.ReadingRoomBookUser

    class Meta:
        model = models.ReadingRoomBookUser
        fields = "__all__"

    def validate(self, data):
        reading_room_book_user = self.instance
        reading_room_book = reading_room_book_user.reading_room_book

        print(reading_room_book, reading_room_book.get_avaliable_stock())
        if reading_room_book.get_avaliable_stock() < 1:
            raise serializers.ValidationError({"error":
                                               "This book is out of stock in this reading room"})
        return data


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
