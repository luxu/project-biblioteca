from django.urls import path

from . import views as v

urlpatterns = [
    path('', v.Index.as_view(), name='index'),

    path('livros/', v.BookListView.as_view(), name='book_list'),
    path('livros/create/', v.BookCreateView.as_view(), name='book_create'),
    path('livros/<int:pk>/edit/', v.BookUpdateView.as_view(), name='book_edit'),
    path('livros/<int:pk>/delete/', v.BookDeleteView.as_view(), name='book_delete'),

    path('autores/', v.AuthorListView.as_view(), name='author_list'),
    path('autores/create/', v.AuthorCreateView.as_view(), name='author_create'),
    path('autores/<int:pk>/edit/', v.AuthorUpdateView.as_view(), name='author_edit'),
    path('autores/<int:pk>/delete/', v.AuthorDeleteView.as_view(), name='author_delete'),
]
