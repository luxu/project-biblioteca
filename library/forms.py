from django.forms import ModelForm

from library.models import Book, Author


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'author'
        ]


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = [
            'name',
        ]
