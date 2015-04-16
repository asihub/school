from django.db import models

class Library(models.Model):
    
    title = models.CharField(max_length=60, verbose_name="Назва")
    description = models.CharField(max_length=200, verbose_name="Опис", blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["title"]
        
class Book(models.Model):
    
    library = models.ForeignKey(Library, verbose_name="Бібліотека")
    title = models.CharField(max_length=60, verbose_name="Назва")       
    author = models.CharField(max_length=60, verbose_name="Автор книги", blank=True)
    year = models.SmallIntegerField(blank=True, null=True, verbose_name="Рік")
    file = models.FileField(upload_to="library/files/", verbose_name="Файл")
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["title"]
        

    
