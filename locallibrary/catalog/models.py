from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.
class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    """
    Foreign Key used because book can only have one author, but authors can have multiple books
    使用外鍵是因為書只能有一個作者，但作者可以有多本書
    null=True 表示如果沒有作者的話，允許在資料庫中存入 Null 值
    on_delete=models.SET_NULL 表示如果某筆作者紀錄被刪除的話，與該作者相關連的欄位都會被設成 Null
    """
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    """
    使用 ManyToManyField 是因為 genre 可以包含很多書。 書籍可以涵蓋多種類型。
    Genre class has already been defined so we can specify the object above.
    """

    def __str__(self):
        """String for representing the Model object."""
        return self.title

