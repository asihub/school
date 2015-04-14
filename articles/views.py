from django.shortcuts import render, get_object_or_404
from articles.models import Articles
from django.core.paginator import Paginator

def articles(request, page=1):
     
    pages = Paginator(Articles.objects.all(), 2)
    
    context = {'articles': pages.page(page)}
    return render(request, 'articles/articles.html', context)

def article(request, article_id=0):
    a = get_object_or_404(Articles, pk=article_id)    
    return render(request, 'articles/article.html', {'a': a}) 