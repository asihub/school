from django.db import models

class DaysOfWeek(models.Model):
    dayNum = models.IntegerField()
    dayName = models.CharField(max_length=20)
    
    def __str__(self):
        return self.dayName
    
    class Meta:
        ordering = ["dayNum"]
        

class Lessons(models.Model):
    
    lesson = models.CharField(max_length=40, verbose_name="Урок")
    
    def __str__(self):
        return self.lesson
    
    class Meta:
        ordering = ["lesson"] 

class Timetable(models.Model):
    
#     Lessons = [ 
#         ("Інформатика", "Інформатика"),
#         ("Історія України", "Історія України"),
#         ("Англійська мова", "Англійська мова"),
#         ("Біологія", "Біологія"),
#         ("Виховна", "Виховна"),
#         ("Географія", "Географія"),
#         ("Логіка", "Логіка"),
#         ("Малювання", "Малювання"),
#         ("Математика", "Математика"),
#         ("Музика", "Музика"),
#         ("Німецька мова", "Німецька мова"),
#         ("Основи здоров'я", "Основи здоров'я"),
#         ("Праця", "Праця"),
#         ("Світова література","Світова література"),
#         ("Українська література", "Українська література"),
#         ("Українська мова", "Українська мова"),
#         ("Фізкультура", "Фізкультура"),
#     ]
    
#     DaysOfWeek = [
#         ("Понеділок", "Понеділок"),
#         ("Вівторок", "Вівторок"),
#         ("Середа", "Середа"),
#         ("Четвер", "Четвер"),
#         ("П'ятниця", "П'ятниця"),
#         ("Субота", "Субота"),
#     ]
    
    LessonNumbers = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
    ]
    
    Parity = [
        ("0", "П+Н"),
        ("1", "Н"),
        ("2", "П"),
    ]
    
    lesson = models.ForeignKey(Lessons)
    
#     dayOfWeek = models.CharField(max_length=10, 
#                                  choices=DaysOfWeek)
    
    lessonNumber = models.IntegerField(choices=LessonNumbers,
                                       default=0)
    
    room = models.CharField(max_length=2)
    begin_time = models.TimeField()
    end_time = models.TimeField()    
    week_parity = models.CharField(max_length=1,
                                   choices=Parity,
                                   default="П+Н")
    
    dayOfWeek = models.ForeignKey(DaysOfWeek)

    def __str__(self):
        return "{}: {} - {}".format(self.dayOfWeek, self.lessonNumber, self.lesson)
    
    class Meta:
        ordering = ["dayOfWeek", "lessonNumber", "lesson"]
        
