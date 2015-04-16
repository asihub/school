from django.db import models
from django.contrib.auth.models import User 

class Galery(models.Model):
   
    status_choices = (
                      (0, "Відключений"),
                      (1, "Загальний"),
                      (2, "Тільки для користувачів"),
                     )

    title = models.CharField(max_length=200, verbose_name="Назва альбому")
    description = models.CharField(max_length=200, verbose_name="Опис", blank=True)
    status = models.IntegerField(default=2, choices=status_choices, verbose_name="Статус")    
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name="Автор")
   
    def __str__(self):
        return self.title
   
    class Meta:
        ordering = ["timestamp"] 

class Album(models.Model):
      
    album = models.ForeignKey(Galery, verbose_name="Альбом")
    photo = models.ImageField(upload_to="galery/photo/", verbose_name="Фотографія")
    description = models.CharField(max_length=200, verbose_name="Коментар", blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")
    user = models.ForeignKey(User, verbose_name="Автор")
      
    def __str__(self):
        return self.photo.url
    
    