from django.db import models
from django.contrib.auth.models import User 

class Vote(models.Model):

    status_choices = (
                      (0, "Неактивний"),
                      (1, "Активний"),
                      )
    
    title = models.CharField(max_length=200, verbose_name="Назва")
    description = models.CharField(max_length=200, verbose_name="Опис", blank=True)
    status = models.IntegerField(default=1, choices=status_choices, verbose_name="Статус")
    user = models.ForeignKey(User, verbose_name="Автор")
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
   
    class Meta:
        ordering = ["title"]  

class Answer(models.Model):
    
    title = models.CharField(max_length=200, verbose_name="Відповідь")
    vote = models.ForeignKey(Vote)
    users = models.ManyToManyField(User, through="Result")
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["title",]
        
class Result(models.Model):
    
    answer = models.ForeignKey(Answer)
    user = models.ForeignKey(User)
            