from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.sections),
    url(r'^(?P<section_id>\d+)/$', views.topics),
    url(r'^(?P<section_id>\d+)/(?P<topic_id>\d+)/$', views.posts),
    url(r'^(?P<section_id>\d+)/(?P<topic_id>\d+)/addpost/$', views.addpost),
    url(r'^(?P<section_id>\d+)/addtopic/$', views.addtopic),
]

