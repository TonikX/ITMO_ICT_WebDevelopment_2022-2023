from django.contrib import admin
from .models import *

admin.site.register(BookCategory)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Authorship)
admin.site.register(Edition)
admin.site.register(OrderManager)
admin.site.register(Customer)
admin.site.register(BooksOrder)
admin.site.register(OrderBook)
