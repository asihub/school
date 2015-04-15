
from django.forms import ModelForm
from .models import Library, Book

class AddBookForm(ModelForm):
     
    class Meta:
        model = Book
        fields = ("library", "title", "year", "file")

