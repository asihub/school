from django.db import models

# --- Міроприємства ---
class Event(models.Model):
    
    status_choices = (
                      (0, "Відмінено"),
                      (1, "Заплановано"),
                      )
        
    title = models.CharField(max_length=150, verbose_name="Міроприємство")    
    ev_date = models.DateField(verbose_name="Час проведення")
    ev_time = models.TimeField(verbose_name="Час проведення")
    place = models.CharField(max_length=150, verbose_name="Місце проведення")
    status = models.BooleanField(verbose_name="Статус", choices=status_choices, default="1")
    author = models.CharField(max_length=40, verbose_name="Автор")
    note = models.TextField(verbose_name="Примітка", blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["ev_date"]