from django.shortcuts import render, redirect
from .forms import AddBookForm, SearchForm
from .models import Book


def library(request):
    
    if request.method=="POST":
        
        if "add_btn" in request.POST:
            
            dataset = Book.objects.all()
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
                    dataset = Book.objects.filter(title__contains=search_text)
            else:
                dataset = Book.objects.all()
                
    else:
        
        form = AddBookForm()
        dataset = Book.objects.all()
        search_form = SearchForm()
    

    context = {"title": "Бібліотека", 
               "form": form, 
               "dataset": dataset, 
               "search_form": search_form,
               }       
    
    return render(request, "library/library.html", context)
