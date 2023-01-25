from django.contrib import admin

from .models import User, Product, SaleRecord


@admin.register(User, Product, SaleRecord)
class Admin(admin.ModelAdmin):
	pass
