from django.shortcuts import render, redirect
from .models import Galery, Photo
from .forms import GaleryForm, PhotoForm
from PIL import Image

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
            
            # Зберігаєм без мініатюри
            photo = form.save(commit=False)
            photo.galery_id = galery_id
            photo.user = request.user            
            photo.save()

            # добавляєм мініатюру
            thumb_path = get_thumb_path(photo.photo.path)
            photo.thumbnail = thumb_path
            
            img = Image.open(photo.photo.path)
            img.thumbnail((128, 128), Image.ANTIALIAS)                        
            img.save(thumb_path, 'JPEG')            
            
            photo.save()
            
            return redirect(".")
    else:
        form = PhotoForm()
    
    dataset = Photo.objects.filter(galery_id=galery_id)
    
    title = "Альбом"
    context = {"title": title, "form": form, "dataset": dataset}
    return render(request, "galery/album.html", context)
    
def get_thumb_path(s):
    parts = s.split(".")
    parts.insert(-1, "_mini.")
    return "".join(parts)