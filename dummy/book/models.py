from django.db import models
from multiselectfield import MultiSelectField


class Book(models.Model):
    name = models.CharField(max_length = 100)
    rating = models.PositiveIntegerField(default = 0)
    PUBLISHED = (('D','Draft'),('P','Published'))
    published = models.CharField(max_length = 2,choices = PUBLISHED)
    GENRE = (('R','Romance'),('D','Drama'),('F','Fiction'),('M','Mystery'))
    genre = MultiSelectField(choices = GENRE)

    def __str__(self):
        return self.name