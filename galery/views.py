from django.shortcuts import render, redirect
from .models import Galery
from .forms import GaleryForm

def galery(request):
    
    form = GaleryForm(request.POST or None)
    if form.is_valid():
        album = form.save(commit=False)
        album.user = request.user
        album.save()
        return redirect(".")
    
    dataset = Galery.objects.all()    
    
    context = {
               "title": "Альбоми", 
               "dataset": dataset, 
               "form": form,
               }
        
    return render(request, "galery/galery.html", context)

def album(request, album_id=1):
    
    
    title = "Альбом"
    context = {"title": title}
    return render(request, "galery/album.html", context)
    
    