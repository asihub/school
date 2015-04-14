from django.contrib import admin
from timetable.models import Timetable, DaysOfWeek, Lessons

admin.site.register(DaysOfWeek)   
admin.site.register(Timetable)    
admin.site.register(Lessons) 
    
