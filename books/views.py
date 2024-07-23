from django.shortcuts import redirect, render
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
    
    return render(req, 'books.html', {'books': books})

def get_books_by_author(req, name):
    try:
        books =  models.Book.objects.filter(author__name = name)
    except models.Book.DoesNotExist:
        books = None
    return render(req, 'books.html', {'books': books})


def get_all_books(req):
    books = models.Book.objects.all()
    categories = {}
    for book in books:
        if book.category not in categories:
            categories[book.category] = []
        categories[book.category].append(book)
    
    return render(req, 'home.html', {'categories': categories})


def delete_book(req, book_id):
    book = models.Book.objects.get(id=book_id)
    book.delete()
    return redirect('books')
