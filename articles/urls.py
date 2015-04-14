from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.articles),
    url(r'^page/(?P<page>\d+)/$', views.articles),
    url(r'^(?P<article_id>\d+)/$', views.article),
]

