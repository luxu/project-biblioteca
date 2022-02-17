from django.urls import reverse_lazy
from django.views import generic as g

from library.forms import BookForm
from library.models import Book


class Index(g.TemplateView):
    template_name = 'index.html'


class BookListView(g.ListView):
    model = Book
    template_name = 'library/book_list.html'
    paginate_by = 10


class AuthorListView(g.ListView):
    model = Book
    template_name = 'library/author_list.html'
    paginate_by = 10


class BookCreateView(g.CreateView):
    model = Book
    template_name = 'library/book_form.html'
    form_class = BookForm
    success_url = 'book_list'


class BookUpdateView(g.UpdateView):
    model = Book
    template_name = 'library/book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('book_list')


class BookDeleteView(g.DeleteView):
    model = Book
    template_name = "library/book_confirm_delete.html"
    success_url = reverse_lazy('book_list')
