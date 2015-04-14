from django.db import models

# --- Розділи форуму ---
class Section(models.Model):
    
    title = models.CharField(max_length=100, verbose_name="Розділ")
    description = models.CharField(max_length=200, verbose_name="Опис")
    order = models.IntegerField(verbose_name="Порядок")    
    
    def __str__(self):
        return "{}: {}".format(self.order, self.title)
    
    class Meta:
        ordering = ['order']
# ---


# --- Теми форуму ---
class Topic(models.Model):
    
    title = models.CharField(max_length=100, verbose_name="Тема")
    description = models.CharField(max_length=200, verbose_name="Опис")
    timestamp = models.DateTimeField(verbose_name="Час створення")
    author = models.CharField(max_length=40, verbose_name="Автор")
    section = models.ForeignKey(Section)
    
    def __str__(self):
        return "{} ({})".format(self.title, self.description)
    
    class Meta:
        ordering = ['timestamp']
# ---
    
# --- Пости ---
class Post(models.Model):
    
    body = models.TextField(max_length=600, verbose_name="Повідомлення")
    timestamp = models.DateTimeField(verbose_name="Час створення", blank=True, null=True)
    author = models.CharField(max_length=40, verbose_name="Автор")
    topic = models.ForeignKey(Topic) 

    def __str__(self):
        return "{} ({}...)".format(self.author, self.body[:100])
    
    class Meta:
        ordering = ['timestamp']  

# ---