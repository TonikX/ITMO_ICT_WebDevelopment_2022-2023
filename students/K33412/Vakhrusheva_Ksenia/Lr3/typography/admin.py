from django.contrib import admin

from .models import User, Author, Manager, Editor, Customer, Book, BookAuthorship, BookEditorship, Order, Contract


@admin.register(User, Author, Manager, Editor, Customer, Book, BookAuthorship, BookEditorship, Order, Contract)
class Admin(admin.ModelAdmin):
	pass
