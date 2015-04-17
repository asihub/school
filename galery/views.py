from django.shortcuts import render, redirect
from .models import Galery, Photo
from .forms import GaleryForm, PhotoForm

def galery(request):
    
    form = GaleryForm(request.POST or None)
    
    if form.is_valid():
        galery = form.save(commit=False)
        galery.user = request.user
        galery.save()
        return redirect(".")
    
    dataset = Galery.objects.all()    
    
    context = {
               "title": "Альбоми", 
               "dataset": dataset, 
               "form": form,
               }
        
    return render(request, "galery/galery.html", context)

def album(request, galery_id=1):
    
    if request.method=="POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            #photo = form.save(commit=False)
            #photo.galery_id = galery_id
            #photo.user = request.user
            form.save()
            return redirect(".")
    else:
        form = PhotoForm()
    
    
    
    title = "Альбом"
    context = {"title": title, "form": form}
    return render(request, "galery/album.html", context)
    
    