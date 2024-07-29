from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def get_books(req):
    books = Book.objects.all()
    if books.exists():
        serialized_books = BookSerializer(books, many = True)
        return Response(serialized_books.data)
    return Response('There are no books')

@api_view(['GET'])
def get_book_by_name(req, name):
    try:
        book = Book.objects.get(title = name)
        serialized_book = BookSerializer(book)
        return Response(serialized_book.data)
    except Book.DoesNotExist:
        return Response('there is no such a book')
    
@api_view(['GET'])
def get_books_by_category(req, cat):
    books = Book.objects.filter(category = cat)
    if books.exists():
        serialized_books = BookSerializer(books, many = True)
        return Response(serialized_books.data)
    return Response('there is no such a book')
    
@api_view(['GET'])
def get_books_by_author(req, name):
    books = Book.objects.filter(author__name = name)
    if books.exists():
        serialized_books = BookSerializer(books, many = True)
        return Response(serialized_books.data)
    return Response('there is no such a book')