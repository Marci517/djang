from django.shortcuts import render
from . import models

def get_book_by_name(req, name):
    try:
        books =  models.Book.objects.get(title = name)
    except models.Book.DoesNotExist:
        books = None
    return render(req, 'book.html', {'book': books})

def get_books_by_category(req, category):
    try:
        books =  models.Book.objects.filter(category = category)
    except models.Book.DoesNotExist:
        books = None

    if len(books) == 1:
        return render(req, 'book.html', {'book': books.first()})
    
    return render(req, 'books.html', {'books': books})

def get_books_by_author(req, name):
    try:
        books =  models.Book.objects.filter(author__name = name)
    except models.Book.DoesNotExist:
        books = None

    if len(books) == 1:
        return render(req, 'book.html', {'book': books.first()})
    
    return render(req, 'books.html', {'books': books})
