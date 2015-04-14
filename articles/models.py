from django.db import models


# --- Категорії статтей ---
class Categories(models.Model):
    
    description = models.CharField(max_length=60)
    
    def __str__(self):
        return self.description
    

# --- Статті ---
class Articles(models.Model):
        
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    source = models.URLField(blank=True)
    status = models.BooleanField()
    category = models.ForeignKey(Categories)
    
    def __str__(self):
        return self.title


        