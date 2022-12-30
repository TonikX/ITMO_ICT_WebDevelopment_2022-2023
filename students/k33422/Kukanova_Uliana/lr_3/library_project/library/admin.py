from django.contrib import admin
from .models import Book, Author, Publisher, Section, Reader, Library, Room, LibraryRoom, ReaderBook, BookRoom, ReaderRoom, User

class Book_Admin(admin.ModelAdmin):
    pass

class User_Admin(admin.ModelAdmin):
    pass

class BookRoom_Admin(admin.ModelAdmin):
    pass

class Author_Admin(admin.ModelAdmin):
    pass

class Publisher_Admin(admin.ModelAdmin):
    pass

class Section_Admin(admin.ModelAdmin):
    pass

class Reader_Admin(admin.ModelAdmin):
    pass

class ReaderRoom_Admin(admin.ModelAdmin):
    pass

class ReaderBook_Admin(admin.ModelAdmin):
    pass

class Library_Admin(admin.ModelAdmin):
    pass

class Room_Admin(admin.ModelAdmin):
    pass

class LibraryRoom_Admin(admin.ModelAdmin):
    pass

admin.site.register(Book, Book_Admin)
admin.site.register(BookRoom, BookRoom_Admin)
admin.site.register(Author, Author_Admin)
admin.site.register(Publisher, Publisher_Admin)
admin.site.register(Section, Section_Admin)
admin.site.register(Reader, Reader_Admin)
admin.site.register(ReaderRoom, ReaderRoom_Admin)
admin.site.register(ReaderBook, ReaderBook_Admin)
admin.site.register(Library, Library_Admin)
admin.site.register(Room, Room_Admin)
admin.site.register(User, User_Admin)
admin.site.register(LibraryRoom, LibraryRoom_Admin)
