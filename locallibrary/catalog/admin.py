from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language


# Register your models here.
# admin.site.register(Book)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance    # 顯示關聯記錄在同一頁


class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book    # 顯示關聯記錄在同一頁


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    """
    我們無法直接在 list_display 中指定「書籍類別」(genre field)字段，因為它是一個 ManyToManyField (多對多字段)，
    因為如果這樣做會造成很大的資料庫讀寫「成本」，所以 Django 會預防這樣的狀況發生，因此，
    取而代之，我們將定義一個 display_genre 函式以「字串」形式得到書籍類別。
    """
    inlines = [BooksInstanceInline]   # 顯示 BookInstance 關聯記錄在同一頁


# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    # 默認情況下，字段是垂直顯示的，但是如果您進一步將它們分組到一個元組中，它們將水平顯示
    inlines = [BooksInline]    # 顯示 Book 關聯記錄在同一頁


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# admin.site.register(BookInstance)
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    # 對於BookInstance列表視圖(list view)，添加代號以顯示books，status，due back date和id（而不是默認的__str__()文本）
    list_filter = ('status', 'due_back')  # 加入列表過濾器 (List Filter)
    # 改變布局
    fieldsets = (
        (None, {  # 不要標題時用 None
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


admin.site.register(Language)
admin.site.register(Genre)
