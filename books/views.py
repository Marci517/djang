from django.shortcuts import render
from django.http import HttpResponse

def say_hello(req):
    x = 1
    y = 2
    return render(req, 'hello.html', {'name': 'Ali'})
