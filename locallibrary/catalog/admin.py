from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language
# Register your models here.
# admin.site.register(Book)
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# admin.site.register(BookInstance)
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Language)
admin.site.register(Genre)