from django.shortcuts import render, redirect
from .forms import AddBookForm, SearchForm
from .models import Book, Library

def library(request):
    
    dataset = Library.objects.all()
    title = "Розділи бібліотеки"
    
    search_form = SearchForm(request.POST or None)
    if search_form.is_valid():
        if "search_text" in search_form.cleaned_data:
            search_text = search_form.cleaned_data["search_text"]
            dataset = dataset.filter(title__contains=search_text)       
    
    context = {"dataset": dataset, 
               "title": title, 
               "search_form": search_form}
        
    return render(request, "library/library.html", context)


def books(request, lib_id=1):
    
    dataset = Book.objects.filter(library_id=lib_id)
    
    if request.method=="POST":
        
        if "add_btn" in request.POST:
            
            search_form = SearchForm()            
            
            form = AddBookForm(request.POST, request.FILES)
            if form.is_valid():            
                form.save()
                return redirect(".")
            
        if "search_btn" in request.POST:
            
            form = AddBookForm()
            search_form = SearchForm(request.POST)
            
            if search_form.is_valid():
                if "search_text" in search_form.cleaned_data:
                    search_text = search_form.cleaned_data["search_text"]
                    dataset = dataset.filter(title__contains=search_text)
                
    else:
        
        form = AddBookForm()        
        search_form = SearchForm()
    

    context = {"title": "Книги", 
               "form": form, 
               "dataset": dataset, 
               "search_form": search_form,
               }       
    
    return render(request, "library/books.html", context)
