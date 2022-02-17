from django.urls import reverse_lazy
from django.views import generic as g

from library.forms import BookForm, AuthorForm
from library.models import Book, Author


class Index(g.TemplateView):
    template_name = 'index.html'


# BOOKS

class BookListView(g.ListView):
    model = Book
    template_name = 'library/book/book_list.html'
    paginate_by = 10


class BookCreateView(g.CreateView):
    model = Book
    template_name = 'library/book/book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('book_list')


class BookUpdateView(g.UpdateView):
    model = Book
    template_name = 'library/book/book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('book_list')


class BookDeleteView(g.DeleteView):
    model = Book
    template_name = "library/book/book_confirm_delete.html"
    success_url = reverse_lazy('book_list')


# AUTHOR

class AuthorListView(g.ListView):
    model = Author
    template_name = 'library/author/author_list.html'
    paginate_by = 10


class AuthorCreateView(g.CreateView):
    model = Author
    template_name = 'library/author/author_form.html'
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')


class AuthorUpdateView(g.UpdateView):
    model = Author
    template_name = 'library/author/author_form.html'
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')


class AuthorDeleteView(g.DeleteView):
    model = Author
    template_name = "library/author/author_confirm_delete.html"
    success_url = reverse_lazy('author_list')
