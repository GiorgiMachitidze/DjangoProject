from django.contrib import admin
from django.urls import path, include
from .views import get_books, get_book, get_authors, get_author, get_categories, get_category

app_name = 'market'

urlpatterns = [
    path('books/', get_books, name='get_books'),
    path('books/<int:book_id>/', get_book, name='get_book'),
    path('category/', get_categories, name='get_categories'),
    path('category/<int:category_id>/', get_category, name='get_category'),
    path('author/', get_authors, name='get_authors'),
    path('author/<int:author_id>/', get_author, name='get_author'),
]
