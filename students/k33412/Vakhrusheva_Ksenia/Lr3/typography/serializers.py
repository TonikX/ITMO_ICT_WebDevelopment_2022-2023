import typing

from django.contrib.auth import get_user_model
from django.db.models import Count
from rest_framework import serializers

from .models import Author, Manager, Editor, Customer, Book, BookAuthorship, Contract, Order

User = get_user_model()


# AUTHOR INDEPENDENT

class AuthorUserSerializer(serializers.ModelSerializer):
	user = serializers.IntegerField()

	class Meta:
		model = Author
		fields = ["user"]


class AuthorPseudonymSerializer(serializers.ModelSerializer):
	user = serializers.SlugRelatedField("id", read_only=True)

	class Meta:
		model = Author
		fields = ["user", "pseudonym"]


class AuthorshipSerializer(serializers.ModelSerializer):
	author = AuthorPseudonymSerializer()

	class Meta:
		model = BookAuthorship
		fields = ["author", "priority"]

	def to_representation(self, instance):
		response = super().to_representation(instance)
		author = response["author"]
		del response["author"]
		response = {**author, **response}
		return response


class UpdateAuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ["pseudonym"]


# BOOK INDEPENDENT


class BookNameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ["id", "name"]


class BookContractsSerializer(serializers.ModelSerializer):
	contracts = serializers.SerializerMethodField()

	class Meta:
		model = Book
		fields = ["id", "name", "contracts"]

	def get_contracts(self, book: Book):
		return book.contracts.count()


# USER INDEPENDENT


class FullUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["id", "username", "first_name", "last_name"]


# AUTHOR ON INDEPENDENT

class PublicAuthorSerializer(serializers.ModelSerializer):
	user = serializers.SlugRelatedField("id", read_only=True)
	books = BookNameSerializer(many=True, read_only=True)

	class Meta:
		model = Author
		fields = ["user", "pseudonym", "books"]


class PrivateAuthorSerializer(serializers.ModelSerializer):
	user = serializers.SlugRelatedField("id", read_only=True)
	books = BookContractsSerializer(many=True)

	class Meta:
		model = Author
		fields = ["user", "pseudonym", "books"]


# BOOK ON INDEPENDENT


class PublicBookSerializer(serializers.ModelSerializer):
	authorships = AuthorshipSerializer(many=True)

	class Meta:
		model = Book
		fields = ["id", "name", "authorships", "pages", "illustrated"]

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response["authors"] = [
			{"user": authorship["user"], "pseudonym": authorship["pseudonym"]}
			for authorship in sorted(response["authorships"], key=lambda x: x["priority"])
		]
		del response["authorships"]
		return response


class UpdateBookSerializer(serializers.ModelSerializer):
	authors = AuthorUserSerializer(many=True)

	class Meta:
		model = Book
		fields = ["name", "authors", "pages", "illustrated"]

	def check_authors_ids(self, authors: typing.List[typing.Dict[str, int]]):
		final_author_ids = set(
			author.get("user")
			for author in authors
			if Author.objects.filter(user=author.get("user")).exists()
		)
		return final_author_ids

	def update(self, book: Book, validated_data):
		if "authors" in validated_data:
			author_ids = self.check_authors_ids(
				validated_data.pop("authors", [])
			)
			book.authors.clear()
			for i, author_id in enumerate(author_ids):
				book.authors.add(author_id, through_defaults={"priority": i})

		fields = ["name", "pages", "illustrated"]
		for field in fields:
			try:
				setattr(book, field, validated_data[field])
			except KeyError:
				pass
		book.save()
		return book


# CONTRACT ON INDEPENDENT

class PublicCustomerSerializer(serializers.ModelSerializer):
	user = FullUserSerializer(read_only=True)

	class Meta:
		model = Customer
		fields = ["user"]

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response = response["user"]
		return response


# EDITORS ON INDEPENDENT


class PublicEditorSerializer(serializers.ModelSerializer):
	user = FullUserSerializer()

	class Meta:
		model = Editor
		fields = ["user"]

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response = response["user"]
		return response


class PrivateEditorSerializer(serializers.ModelSerializer):
	books = PublicBookSerializer(many=True)
	user = FullUserSerializer()

	class Meta:
		model = Editor
		fields = ["user", "books"]


# MANAGER ON INDEPENDENT

class PublicManagerSerializer(serializers.ModelSerializer):
	user = FullUserSerializer(read_only=True)

	class Meta:
		model = Manager
		fields = ["user"]

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response = response["user"]
		return response


# CONTRACT

class ManagerlessContractSerializer(serializers.ModelSerializer):
	book = PublicBookSerializer()

	class Meta:
		model = Contract
		fields = ["id", "book", "creation_datetime"]


class ContractSerializer(serializers.ModelSerializer):
	book = PublicBookSerializer()
	manager = PublicManagerSerializer()

	class Meta:
		model = Contract
		fields = ["id", "book", "manager", "creation_datetime"]


class SimpleContractSerializer(serializers.ModelSerializer):
	book = serializers.IntegerField()

	class Meta:
		model = Contract
		fields = ["book"]


# BOOK

class PrivateBookSerializer(serializers.ModelSerializer):
	authorships = AuthorshipSerializer(many=True)
	main_editor = PublicEditorSerializer()
	editors = PublicEditorSerializer(many=True)

	class Meta:
		model = Book
		fields = ["id", "name", "authorships", "main_editor", "editors", "pages", "illustrated"]

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response["authorships"] = sorted(response["authorships"], key=lambda x: x["priority"])
		return response


# MANAGER


class PrivateManagerSerializer(serializers.ModelSerializer):
	user = FullUserSerializer(read_only=True)
	contracts = ManagerlessContractSerializer(many=True)

	class Meta:
		model = Manager
		fields = ["user", "contracts"]


# ORDER

class OrderSerializer(serializers.ModelSerializer):
	contracts = ContractSerializer(many=True)

	class Meta:
		model = Order
		fields = ["id", "contracts"]


class FullOrderSerializer(serializers.ModelSerializer):
	contracts = ContractSerializer(many=True)
	customer = PublicCustomerSerializer()

	class Meta:
		model = Order
		fields = ["id", "customer", "contracts"]


class CreateOrderSerializer(serializers.ModelSerializer):
	contracts = SimpleContractSerializer(many=True)
	customer = PublicCustomerSerializer(read_only=True)

	class Meta:
		model = Order
		fields = ["contracts", "customer"]

	def check_book_ids(self, contracts):
		book_ids = set(
			contract.get("book")
			for contract in contracts
			if Book.objects.filter(id=contract.get("book")).exists()
		)
		return book_ids

	def create(self, validated_data):
		book_ids = self.check_book_ids(
			validated_data.pop("contracts", [])
		)
		managers = Manager.objects.values("user").annotate(Count("contracts"))
		order = Order.objects.create(customer=validated_data.get("customer"))
		for i, book_id in enumerate(book_ids):
			manager = sorted(managers, key=lambda x: x.get("contracts__count"))[0]
			Contract.objects.create(order=order, book_id=book_id, manager_id=manager["user"])
			manager["contracts__count"] = manager.get("contracts__count") + 1
		return order


# CUSTOMER

class PrivateCustomerSerializer(serializers.ModelSerializer):
	user = FullUserSerializer(read_only=True)
	orders = OrderSerializer(read_only=True, many=True)

	class Meta:
		model = Customer
		fields = ["user", "orders"]


# User

class UserProfilesSerializer(serializers.ModelSerializer):
	author = AuthorPseudonymSerializer()
	manager = PublicManagerSerializer()
	editor = PublicEditorSerializer()
	customer = PublicCustomerSerializer()

	class Meta:
		model = User
		fields = ["author", "manager", "editor", "customer"]
