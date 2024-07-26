from django.urls import path
from . import views

urlpatterns = [
    path('jsonbooks/', views.get_books)
]