from django.contrib.auth.hashers import make_password
from operator import itemgetter
from rest_framework import serializers

from . import models


class ModelSerializer(serializers.ModelSerializer):
    model = None

    class Meta:
        model = None
        depth = 1

    # https://stackoverflow.com/questions/37445248/how-to-dynamically-change-depth-in-django-rest-framework-nested-serializers
    def __init__(self, *args, **kwargs):
        depth = kwargs.pop("meta_depth", None)
        drop_fields = kwargs.pop("drop_fields", None)
        super(ModelSerializer, self).__init__(*args, **kwargs)

        if depth is not None:
            self.Meta.depth = depth

        if drop_fields is not None:
            for field_name in drop_fields:
                self.fields.pop(field_name)

    def create(self, validated_data):
        object = self.model(**validated_data)
        object.save()
        return object

    def validate(self, data):
        return data


class LibrarySerializer(ModelSerializer):
    model = models.Library

    def __init__(self, depth, *args, **kwargs):
        super(LibrarySerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = models.Library
        fields = [
            "id",
            "name",
            "readingroom_set",
            "user_set"
        ]
        depth = 10


class ReadingRoomSerializer(ModelSerializer):
    model = models.ReadingRoom

    class Meta:
        model = models.ReadingRoom
        fields = "__all__"

    def validate(self, data):
        reading_room = self.instance
        capacity = data.get("capacity")
        if capacity is not None:
            users = reading_room.get_all_users()

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

        if book:
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
        # fields = "__all__"
        fields = [
            "id",
            "book",
            "borrowers",
            "reading_room",
            "stock",
            "readingroombookuser_set"
        ]
        depth = 2

    def validate(self, data):
        reading_room_book = self.instance
        if hasattr(reading_room_book, 'book'):
            book = reading_room_book.book
        else:
            book = data.get("book")

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
        # reading_room_book_user = self.instance
        # print("reading_room_book_user", reading_room_book_user)

        # is_a_new_entry = reading_room_book_user is None

        # if is_a_new_entry:
        #     print("need to check if there are enough books")
        # else:
        #     is_trying_to_borrow = not not reading_room_book_user.returned_date
        #     if is_trying_to_borrow:
        #         print("need to check if there are enough books")
        #     else:
        #         print("dont need to check")
        #         return data

        return data

        # print("reading_room_book_userreading_room_book_user",
        #       reading_room_book_user)

        # if reading_room_book_user:
        #     reading_room_book = reading_room_book_user.reading_room_book
        #     prev_returned_date = reading_room_book_user.returned_date
        #     new_returned_date = data.get("returned_date")
        # else:
        #     reading_room_book = data.get("reading_room_book")

        # is_trying_to_borrow = new_returned_date is None and prev_returned_date is not None
        # if prev_returned_date:
        #     if reading_room_book and is_trying_to_borrow:
        #         if reading_room_book.get_avaliable_stock() < 1:
        #             raise serializers.ValidationError({"error":
        #                                                "This book is out of stock in this reading room"})
        # return data


class UserSerializer(ModelSerializer):
    model = models.User

    class Meta:
        ref_name = "CustomUser"
        model = models.User
        depth = 2

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
            "date_of_birth",
            "library",
            "reading_room",

            "readingroombookuser_set",
        ]
        read_only_fields = ['serial_number']

        extra_kwargs = {'password': {'write_only': True}}

    # Overriden for handling hashing of the password and generating serial number
    def create(self, validated_data):

        # Put list of keys to separate variables, aka destructuring assignment
        password = itemgetter(
            *['password'])(validated_data)
        # Get dict, excluding the keys that were 'taken out'
        rest = {key: validated_data[key]
                for key in validated_data if key not in ['password', 'serial_number']}

        print("validated_data", validated_data)
        print("REST", rest)

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


class GroupedModelsSerializer():
    primarySerializer = None
    secondarySerializer = None

    def __init__(self, initial_grouped_data):
        self.initial_grouped_data = initial_grouped_data

    @property
    def data(self):
        pass


class GroupedLibraryUsersSerializer(GroupedModelsSerializer):
    primarySerializer = LibrarySerializer
    secondarySerializer = UserSerializer

    @property
    def data(self):
        grouped_library = self.initial_grouped_data

        grouped_library_data = {
            "library": {},
            "dates": {}
        }
        for date, users in grouped_library['dates'].items():
            serializer = self.secondarySerializer(users, many=True)
            grouped_library_data['dates'][date] = serializer.data

        serializer = self.primarySerializer(grouped_library['library'])
        grouped_library_data['library'] = serializer.data

        return grouped_library_data


class GroupedReadingRoomsUsersSerializer(GroupedModelsSerializer):
    primarySerializer = ReadingRoomSerializer
    secondarySerializer = UserSerializer

    @property
    def data(self):
        grouped_rooms = self.initial_grouped_data

        grouped_rooms_data = []
        for grouped_room in grouped_rooms:
            grouped_room_data = {
                "reading_room": {},
                "dates": {}
            }
            for date, users in grouped_room['dates'].items():
                serializer = self.secondarySerializer(users, many=True)
                grouped_room_data['dates'][date] = serializer.data

            grouped_rooms_data.append(grouped_room_data)

            serializer = self.primarySerializer(
                grouped_room['reading_room'])
            grouped_room_data['reading_room'] = serializer.data

        return grouped_rooms_data
