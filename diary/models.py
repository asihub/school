from django.db import models
from timetable.models import Lessons

class Diary(models.Model):
    
    lesson = models.ForeignKey(Lessons, verbose_name="Урок")
    hw_date = models.DateField(verbose_name="На котрий день")
    hw_descr = models.CharField(max_length=200, verbose_name="Завдання")
    
    def __str__(self):
        return "{} {}: {}".format(self.hw_date, self.lesson, self.hw_descr)
    
    class Meta:
        ordering = ["hw_date"]

