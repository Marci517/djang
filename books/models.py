from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200, unique=True)
    age = models.PositiveIntegerField(null = True)



class Book(models.Model):
    author =  models.ForeignKey(Author, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200, null = True)

    def __str__(self):
        return self.title