
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, Page

from .models import Book, Author, Category


def get_books(request):
    books = Book.objects.all()
    paginator = Paginator(books, per_page = 2)
    page_num = int(request.GET.get('page', 1))
    page : Page = paginator.get_page(page_num)
    return render(request, 'index.html', {'books': page})



def get_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'detail.html', {'books': [book]})

def get_authors(request):
    authors = Author.objects.all()
    paginator = Paginator(authors, per_page=2)
    page_num = int(request.GET.get('page', 1))
    page: Page = paginator.get_page(page_num)
    return render(request, 'author_index.html', {'authors': page})


def get_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author_detail.html', {'author': author})

def get_categories(request):
    categories = Category.objects.all()
    paginator = Paginator(categories, per_page=2)
    page_num = request.GET.get('page')
    page: Page = paginator.get_page(page_num)
    return render(request, 'category_index.html', {'categories': page})


def get_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    books = category.books.all()
    return render(request, 'category_index.html', {'category': category, 'books': books})