from django.shortcuts import redirect, render
from . import models
from .forms import *

def get_book_by_name(req):
    try:
        form = BookSearchForm(req.GET)
        name = req.GET.get('title')
        if form.is_valid():
            books =  models.Book.objects.get(title = name)
        else:
            return render(req, 'error.html')
    except models.Book.DoesNotExist:
        books = None
    return render(req, 'book.html', {'book': books})

def get_books_by_category(req):
    try:
        form = CategorySearchForm(req.GET)
        category = req.GET.get('category')
        if form.is_valid():
            books =  models.Book.objects.filter(category = category)
        else:
            return render(req, 'error.html')
    except models.Book.DoesNotExist:
        books = None
    
    return render(req, 'books.html', {'books': books})

def get_books_by_author(req):
    try:
        form = AuthorSearchForm(req.GET)
        name = req.GET.get('author')
        if form.is_valid():
            books =  models.Book.objects.filter(author__name = name)
        else:
            return render(req, 'error.html')
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
    return redirect('home')

def create_book(req):
    form = BookForm()
    if req.method == 'POST':
        form = BookForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(req, 'error.html')
    return render(req, 'book_form.html', {'books': form})

def update_book(req, book_id):
    book = models.Book.objects.get(id=book_id)
    form = BookForm(instance=book)
    if req.method == 'POST':
            form = BookForm(req.POST, instance=book)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                return render(req, 'error.html')
    return render(req, 'book_form.html', {'books':form})

def details_book(req, book_id):
    book = models.Book.objects.get(id=book_id)
    return render(req, 'book_details.html', {'book': book})

