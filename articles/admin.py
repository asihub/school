from django.contrib import admin
from articles.models import Articles, Categories

admin.site.register(Categories)

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')
    #fields = ['title', 'body']            
    list_filter = ['timestamp']
    search_fields = ['title']    
    
admin.site.register(Articles, ArticlesAdmin)

