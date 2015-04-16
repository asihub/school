from django.forms import ModelForm
from .models import Galery

class GaleryForm(ModelForm):
     
    class Meta:
        model = Galery  
        fields = ["title", "description", "status"]

