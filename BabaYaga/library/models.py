from django.db import models

# Create your models here.

class Book(models.Model):
    isbn = models.IntegerField(unique=True,)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    total_count = models.IntegerField(default=1)
    available_count = models.IntegerField(default=1)


class Author(models.Model):
    name = models.CharField(max_length=100)
    book = models.ForeignKey('Book', verbose_name="Books", related_name="books", on_delete=models.DO_NOTHING)
