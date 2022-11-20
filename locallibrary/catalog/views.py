from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
# Create your views here.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a') 可借閱的
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    num_genre = Genre.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
    }
    # Render the HTML template index.html with the data in the context variable
    # 調用 render() 函數來創建並返回 HTML 頁面作為響應
    # context 變量包含將插入到這些佔位符中的數據的 Python 字典）為參數
    return render(request, 'index.html', context=context)