from django.contrib import admin
from .models import Book, Library

admin.site.register(Library) 
admin.site.register(Book)
