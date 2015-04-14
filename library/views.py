from django.shortcuts import render

def library(request):    
    
    context = {"title": "Бібліотека"}    
    return render(request, "library/library.html", context)