from django.forms import ModelForm
from .models import *
from django import forms

class BookForm(ModelForm):
    class Meta:
        model=Book
        fields = '__all__'

class BookSearchForm(forms.Form):
    title = forms.CharField(max_length=200, required=True)

class CategorySearchForm(forms.Form):
    category = forms.CharField(max_length=200, required=True)

class AuthorSearchForm(forms.Form):
    author = forms.CharField(max_length=200, required=True)

class RevRatForm(ModelForm):
    class Meta:
        model=RevRat
        fields = '__all__'
        exclude = ['book']