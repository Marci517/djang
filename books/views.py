from django.shortcuts import redirect, render
from . import models
from .models import Book, RevRat
from .forms import *

def get_book_by_name(req):
    try:
        form = BookSearchForm(req.GET)
        name = req.GET.get('title')
        if form.is_valid():
            books =  Book.objects.get(title = name)
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
            books =  Book.objects.filter(category = category)
        else:
            return render(req, 'error.html')
    except Book.DoesNotExist:
        books = None
    
    return render(req, 'books.html', {'books': books})

def get_books_by_author(req):
    try:
        form = AuthorSearchForm(req.GET)
        name = req.GET.get('author')
        if form.is_valid():
            books =  Book.objects.filter(author__name = name)
        else:
            return render(req, 'error.html')
    except Book.DoesNotExist:
        books = None
    return render(req, 'books.html', {'books': books})


def get_all_books(req):
    books = Book.objects.all()
    categories = {}
    for book in books:
        if book.category not in categories:
            categories[book.category] = []
        categories[book.category].append(book)
    
    return render(req, 'home.html', {'categories': categories})

def delete_book(req, book_id):
    book = Book.objects.get(id=book_id)
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
    book = Book.objects.get(id=book_id)
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
    form = RevRatForm()
    book = Book.objects.get(id=book_id)
    all_revrat = RevRat.objects.filter(book = book)
    revrat = None
    overall_rating = None
    if all_revrat:
        revrat = all_revrat[:3]
        overall_rating = sum(review.rating for review in all_revrat) / all_revrat.count()
    return render(req, 'book_details.html', {'book': book, 'reviews': revrat, 'rating': overall_rating, 'revratform': form})

def create_revrat(req, book_id):
    if req.method == 'POST':
        book = Book.objects.get(id=book_id)
        form = RevRatForm(req.POST)
        if form.is_valid():
            form.book = book
            form_with_book = form.save(commit=False)
            form_with_book.book = book
            form_with_book.save()
            return redirect('details_book', book_id)
        else:
            form = RevRatForm() #just for the 'frontend', it show a right message in the same page, not just rendering the error html
            book = Book.objects.get(id=book_id)
            all_revrat = RevRat.objects.filter(book = book)
            revrat = None
            overall_rating = None
            if all_revrat:
                revrat = all_revrat[:3]
                overall_rating = sum(review.rating for review in all_revrat) / all_revrat.count()
            error = 'The rating should be in 1-10'
            return render(req, 'book_details.html', {'book': book, 'reviews': revrat, 'rating': overall_rating, 'revratform': form,
                                                     'error':error})
    return redirect('details_book', book_id)


