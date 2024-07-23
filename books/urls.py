from django.urls import path
from . import views

#URL config

urlpatterns = [
    path('', views.get_all_books),
    path('getBookByName/<str:name>', views.get_book_by_name),
    path('getBooksByAuthor/<str:name>', views.get_books_by_author),
    path('getBooksByCategory/<str:category>', views.get_books_by_category),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]