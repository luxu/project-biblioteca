from django.contrib import admin

from library.models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    list_filter = ['title', 'id']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ...
