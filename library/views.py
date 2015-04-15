from django.shortcuts import render, redirect
from .forms import AddBookForm
from .models import Book


def library(request):

    if request.method == "POST" and "addbtn" in request.POST:
        form = AddBookForm(request.POST, request.FILES)      
        if form.is_valid():            
            form.save()
            return redirect(".")
    else:
        form = AddBookForm()        
    
    if request.method == "POST" and "srchbtn" in request.POST:
        dataset = Book.objects.filter(title="git_magic.pdf")
    else:
        dataset = Book.objects.all()   
     
    context = {"title": "Бібліотека", "form": form, "dataset": dataset}       
    
    return render(request, "library/library.html", context)
