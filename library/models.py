from django.db import models


class Author(models.Model):
    name = models.CharField(
        'Nome do autor',
        max_length=100
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class Book(models.Model):
    title = models.CharField(
        'Título',
        max_length=100
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name='Autor',
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
