from django.urls import path
from . import views

#URL config

urlpatterns = [
    path('', views.get_all_books, name='home'),
    path('getBookByName/', views.get_book_by_name, name='get_book_by_name'),
    path('getBooksByAuthor/', views.get_books_by_author, name='get_books_by_author'),
    path('getBooksByCategory/', views.get_books_by_category, name='get_books_by_category'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('create/', views.create_book, name='create_book'),
    path('update/<int:book_id>/', views.update_book, name='update_book'),
    path('details/<int:book_id>/', views.details_book, name='details_book'),
]