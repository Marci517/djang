from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.get_books),
    path('name/<str:name>/', views.get_book_by_name),
    path('category/<str:cat>/', views.get_books_by_category),
    path('author/<str:name>/', views.get_books_by_author),
    path('create/', views.create_book),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book)
]