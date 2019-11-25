from django.db import models
from book.models import Book


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length = 30)
    dob = models.DateField()
    password = models.CharField(max_length = 60)
    books = models.ManyToManyField(Book, through='Read')    
    
    def __str__(self):
        return self.name

    
class Read(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    STATUS = (('C','Completed'),('R','Reading...'),('CC','Yet to complete'),('NS','Not Started'))
    read_status = models.CharField(choices = STATUS, max_length=4)