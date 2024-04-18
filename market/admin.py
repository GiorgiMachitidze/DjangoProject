from django.contrib import admin

from .models import Book, Author, Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('name', 'author_name')

    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    list_filter = ['first_name', 'last_name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']