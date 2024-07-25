from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    
class RevRat(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null = True)
    user = models.CharField(max_length=200)
    review = models.CharField(max_length=200)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null = True)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']