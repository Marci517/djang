from django.urls import path
from . import views

#URL config

urlpatterns = [
    path('getBookByName/', views.say_hello)
]