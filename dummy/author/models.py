from django.db import models
from book.models import Book


class Author(models.Model):
    name = models.CharField(max_length = 30)
    dob = models.DateField()
    books = models.ManyToManyField(Book, through='Release')
    total_books = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)


class Release(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    release_date = models.DateField()

    def __str__(self):
        return str(self.author)