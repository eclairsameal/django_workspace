from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language
# Register your models here.
# admin.site.register(Book)
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    """
    我們無法直接在 list_display 中指定「書籍類別」(genre field)字段，因為它是一個 ManyToManyField (多對多字段)，
    因為如果這樣做會造成很大的資料庫讀寫「成本」，所以 Django 會預防這樣的狀況發生，因此，
    取而代之，我們將定義一個 display_genre 函式以「字串」形式得到書籍類別。
    """

# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# admin.site.register(BookInstance)
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Language)
admin.site.register(Genre)