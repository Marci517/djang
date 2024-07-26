from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def get_books(req):
    books = Book.objects.all()
    serialized_books = BookSerializer(books, many = True)
    return Response(serialized_books.data)