
from django.forms import ModelForm, Form, CharField
from .models import Library, Book

class AddBookForm(ModelForm):
     
    class Meta:
        model = Book
        fields = ("title", "author", "year", "file")

class SearchForm(Form):
    
    search_text = CharField(max_length=20, label="Текст для пошуку")