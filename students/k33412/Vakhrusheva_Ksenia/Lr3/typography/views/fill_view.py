from random import shuffle, randint, choice

import coolname
import names
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from typography.models import *


@api_view(["post"])
def fill_data(request: Request):
	# Counts

	user_count = 15
	author_count = 5
	editor_count = 5
	manager_count = 5
	customer_count = 5

	book_count = 20
	min_max_authors_per_book = (1, 3)
	min_max_editors_per_book = (1, 3)

	order_count = 20
	min_max_contracts_per_order = (1, 3)

	# Users

	users = [
		User.objects.create_user(username=f"user-{i}",
		                         password="pass",
		                         first_name=names.get_first_name(),
		                         last_name=names.get_last_name())
		for i in range(user_count)
	]

	# Profiles

	shuffle(users)
	authors = [Author.objects.create(user=user, pseudonym=user.get_full_name()) for user in users[:author_count]]
	shuffle(users)
	editors = [Editor.objects.create(user=user) for user in users[:editor_count]]
	shuffle(users)
	managers = [Manager.objects.create(user=user) for user in users[:manager_count]]
	shuffle(users)
	customers = [Customer.objects.create(user=user) for user in users[:customer_count]]

	# Books

	books = [
		Book.objects.create(
			main_editor=choice(editors),
			name=' '.join(x.capitalize() for x in coolname.generate()),
			pages=15,
			illustrated=True
		) for i in range(book_count)
	]

	for book in books:
		shuffle(authors)
		for i, author in enumerate(authors[:randint(min_max_authors_per_book[0], min_max_authors_per_book[1])]):
			book.authors.add(author, through_defaults={"priority": i})

		book.editors.add(book.main_editor)
		shuffle(editors)
		for editor in editors[:randint(min_max_editors_per_book[0], min_max_editors_per_book[1])]:
			book.editors.add(editor)

	# Orders

	orders = [
		Order.objects.create(customer=choice(customers))
		for _ in range(order_count)
	]

	for order in orders:
		for i in range(randint(min_max_contracts_per_order[0], min_max_contracts_per_order[1])):
			book = choice(books)
			Contract.objects.create(
				order=order,
				book=book,
				manager=choice(managers),
			)

	return Response({"message": "ok"})
