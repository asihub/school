from django.forms import ModelForm
from .models import Galery, Photo

class GaleryForm(ModelForm):
     
    class Meta:
        model = Galery  
        fields = ["title", "description", "status"]

class PhotoForm(ModelForm):
    
    class Meta:
        model = Photo
        fields = ["photo", "description"]